(() => {
  'use strict';
  const $ = (s, p = document) => p.querySelector(s);
  const $$ = (s, p = document) => [...p.querySelectorAll(s)];
  const state = { bootstrap: { templates: [], skills: [], sources: [], universe: [] }, projects: [], current: null, dirty: false, library: 'active', pending: null, pendingRevision: null, busy: false, validation: null, historyToken: 0, sourceToken: 0 };
  const fields = ['name','kind','owner','version','purpose','description','audience','inputs','outputs','constraints','instructions'];
  const kinds = { 'custom-gpt':'Custom GPT', 'agent-skill':'Agent Skill', workflow:'Workflow', 'web-tool':'Web tool' };
  const api = async (path, options = {}) => {
    const opts = { headers: { Accept: 'application/json', ...(options.headers || {}) }, ...options };
    if (opts.body) opts.headers = { ...opts.headers, 'Content-Type':'application/json', 'X-Foundry-Request':'1' };
    let response; try { response = await fetch(path, opts); } catch (_) { throw new Error('The local FoundRy service is not available yet. Your text remains on this screen.'); }
    if (!response.ok) { let detail = ''; try { detail = (await response.json()).error; } catch (_) {} throw new Error(detail || `Request failed (${response.status}).`); }
    return response;
  };
  const esc = (value) => String(value ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  let localIdSequence = 0;
  const safeId = () => `local-${typeof globalThis.crypto?.randomUUID === 'function' ? globalThis.crypto.randomUUID() : `${Date.now().toString(36)}-${++localIdSequence}`}`;
  const status = (text, error = false) => { const m = $('#message'); m.textContent = text; m.className = `message global-message${error ? ' error' : ''}`; m.hidden = false; if (error) m.focus(); };
  const clearStatus = () => { $('#message').hidden = true; };
  const setConnection = (ok) => { const c = $('#connection'); c.textContent = ok ? 'Local service ready' : 'Local service unavailable'; c.className = `connection ${ok ? 'ok' : 'bad'}`; };
  const projectCard = (p) => `<button class="project-card${state.current?.id === p.id ? ' active':''}" data-id="${esc(p.id)}"><strong>${esc(p.name || 'Untitled')}</strong><small>${esc(kinds[p.kind] || p.kind)} · r${esc(p.revision ?? 0)}</small></button>`;

  function setBusy(value) {
    state.busy = value;
    $('#workspace').setAttribute('aria-busy', String(value));
    $$('button, input, textarea, select').forEach(control => { control.disabled = value; });
  }
  function invalidateReview() {
    state.validation = null;
    $('#validation-result').innerHTML = '<p>Check readiness for this saved revision. Earlier results are no longer shown.</p>';
    $('#package-inspection').hidden = true;
    $('#package-inspection').replaceChildren();
  }
  function showSaved(project) {
    state.current = project;
    state.saved = structuredClone(project);
    state.dirty = false;
    state.sourceToken++;
    $('#source-viewer').hidden = true;
    $('#save-button').textContent = 'Save draft';
    $('#package-inspection').hidden = true;
    invalidateReview();
    renderCurrent();
    renderLibrary();
  }
  async function refreshAfterSave() {
    try { await refreshProjects(); }
    catch (_) { status('The record was saved, but the library could not refresh. Reopen the page when the service is available.', true); }
  }
  function renderLibrary() { const q = $('#project-search').value.trim().toLowerCase(); const archived = state.library === 'archived'; const projects = state.projects.filter(p => (p.status === 'archived') === archived && `${p.name} ${p.kind}`.toLowerCase().includes(q)); $('#project-list').innerHTML = projects.length ? projects.map(projectCard).join('') : `<p class="muted">${archived ? 'Nothing archived yet.' : 'No matching drafts. Start one above.'}</p>`; $$('.project-card').forEach(b => b.addEventListener('click', () => requestOpen(b.dataset.id))); }
  function templateButton(t) { return `<button type="button" class="template" data-template="${esc(t.id)}"><p class="eyebrow">${esc(kinds[t.project?.kind] || 'Template')}</p><h3>${esc(t.name)}</h3><p>${esc(t.description)}</p></button>`; }
  function renderTemplates() { const markup = state.bootstrap.templates.map(templateButton).join(''); $('#template-grid').innerHTML = markup; $('#dialog-templates').innerHTML = markup; $$('[data-template]').forEach(b => b.addEventListener('click', () => createFromTemplate(b.dataset.template))); }
  function optionList(selected, components) { return components.filter(c => c.id !== selected).map(c => `<option value="${esc(c.id)}">${esc(c.name || c.id)}</option>`).join(''); }
  function renderComponents() { const wrap = $('#components'); const components = state.current?.components || []; wrap.innerHTML = components.length ? components.map((c, i) => `<article class="component" data-index="${i}"><button type="button" class="remove" aria-label="Remove component">Remove</button><div class="component-grid"><label>Name<input data-key="name" value="${esc(c.name)}" placeholder="Component name"></label><label>Reference ID<input data-key="id" readonly value="${esc(c.id)}" placeholder="component-id"></label></div><label>Purpose<textarea data-key="purpose" rows="2" placeholder="What this part makes possible">${esc(c.purpose)}</textarea></label><label>Depends on <select data-key="dependsOn" multiple size="${Math.max(2,Math.min(5,components.length - 1))}">${optionList(c.id, components)}</select></label></article>`).join('') : '<p class="muted">No pieces yet. Add only what helps the project work.</p>';
    $$('.component', wrap).forEach((node, i) => { const c = components[i]; const select = $('[data-key="dependsOn"]', node); [...select.options].forEach(o => o.selected = (c.dependsOn || []).includes(o.value)); $$('.remove', node).forEach(b => b.addEventListener('click', () => { const removed = state.current.components.splice(i,1)[0]; state.current.components.forEach(item => { item.dependsOn = item.dependsOn.filter(id => id !== removed.id); }); markDirty(); renderComponents(); })); $$('[data-key]', node).forEach(control => control.addEventListener('input', () => { c[control.dataset.key] = control.multiple ? [...control.selectedOptions].map(o => o.value) : control.value; markDirty(); })); }); }
  function renderTests() { const wrap = $('#tests'); const tests = state.current?.tests || []; wrap.innerHTML = tests.length ? tests.map((t,i) => `<article class="test" data-index="${i}"><button type="button" class="remove" aria-label="Remove evidence">Remove</button><div class="test-grid"><label>Acceptance case<input data-key="name" value="${esc(t.name)}" placeholder="What should happen?"></label><label>Status<select data-key="status"><option value="not-run">Not run</option><option value="pass">Pass</option><option value="fail">Fail</option></select></label></div><label>Expected result<textarea data-key="expected" rows="2">${esc(t.expected)}</textarea></label><label>Actual observed evidence<textarea data-key="actual" rows="2" placeholder="Record what you actually saw or measured.">${esc(t.actual)}</textarea></label></article>`).join('') : '<p class="muted">No evidence cases yet. Add one when you can describe a useful result.</p>';
    $$('.test', wrap).forEach((node,i) => { const t = tests[i]; $('[data-key="status"]',node).value = t.status || 'not-run'; $('.remove',node).addEventListener('click', () => { state.current.tests.splice(i,1); markDirty(); renderTests(); }); $$('[data-key]',node).forEach(control => control.addEventListener('input', () => { t[control.dataset.key] = control.value; markDirty(); })); }); }
  function renderSkills() { const chosen = new Set(state.current?.skillIds || []); const registered = state.bootstrap.skills || []; const skills = [...registered, ...[...chosen].filter(id => !registered.some(s => s.id === id)).map(id => ({id, name: id, description: 'Reference unavailable. Keep it for provenance or uncheck to detach.'}))]; $('#skills').innerHTML = skills.length ? skills.map(s => `<div class="choice"><input id="skill-${esc(s.id)}" type="checkbox" value="${esc(s.id)}" ${chosen.has(s.id) ? 'checked':''}><label for="skill-${esc(s.id)}"><strong>${esc(s.name)}</strong><span class="muted">${esc(s.description || '')}${s.revision ? ` · ${esc(s.revision)}` : ''}</span></label></div>`).join('') : '<p class="muted">No Skillz reference file is available to this local service.</p>';
    $$('#skills input').forEach(box => box.addEventListener('change', () => { state.current.skillIds = $$('#skills input:checked').map(x => x.value); markDirty(); }));
    $$('#skills input').forEach(box => { const skill = skills.find(item => item.id === box.value); const url = skill && /^https:\/\//.test(skill.url || '') ? skill.url : null; if (url) { const link = document.createElement('a'); link.href = url; link.target = '_blank'; link.rel = 'noopener noreferrer'; link.textContent = `Open pinned source · ${skill.sourcePath || 'path unavailable'}`; box.closest('.choice').querySelector('label').append(document.createElement('br'), link); } });
    $('#sources').innerHTML = (state.bootstrap.sources || []).map(s => `<button type="button" class="source-button" data-source="${esc(s.id)}"><strong>${esc(s.title)}</strong><br><small>${esc(s.description || 'Read-only reference')}</small></button>`).join('') || '<p class="muted">No reference sources are configured.</p>';
    $$('[data-source]').forEach(b => b.addEventListener('click', () => openSource(b.dataset.source)));
  }
  function renderUniverse() {
    const all = state.bootstrap.universe || [];
    const byId = Object.fromEntries(all.map(item => [item.id, item]));
    const required = ['askjamie','overkill','gleefully','skillz','askjamie-foundry','overkill-foundry','gleefully-foundry'];
    if (all.length !== 7 || required.some(id => !byId[id])) {
      $('#universe-map').textContent = 'The seven universe records are unavailable.';
      $('#universe-list').replaceChildren(); return;
    }
    $('#universe-map').innerHTML = `<svg viewBox="0 0 960 445" role="img" aria-labelledby="universe-title universe-description"><title id="universe-title">Three overlapping regions of the OKHP3 universe</title><desc id="universe-description">AskJamie on the left, OverKill at the connective center, Glee-fully on the right. Each has its own FoundRy. Skillz is shared across all three. OverKill Found-Ry stays exclusively in OverKill.</desc><g fill-opacity=".08" stroke-width="3"><circle cx="260" cy="215" r="195" fill="#2d6f7e" stroke="#2d6f7e"/><circle cx="480" cy="215" r="195" fill="#6b5e57" stroke="#6b5e57"/><circle cx="700" cy="215" r="195" fill="#d94f63" stroke="#d94f63"/></g><g text-anchor="middle" fill="#2e2b29"><text x="205" y="140" font-size="27" font-weight="700">AskJamie</text><text x="480" y="97" font-size="27" font-weight="700">OverKill Hill</text><text x="755" y="140" font-size="27" font-weight="700">Glee-fully</text><text x="205" y="190" font-size="17">Helpdesk and lenses</text><text x="205" y="239" font-size="17">AskJamie FoundRy</text><text x="480" y="148" font-size="17">Connective center</text><text x="480" y="208" font-size="18" font-weight="700">OverKill Found-Ry</text><text x="480" y="239" font-size="15">OverKill only</text><text x="755" y="190" font-size="17">Personalizable tools</text><text x="755" y="239" font-size="17">Glee-fully FoundRy</text><rect x="318" y="314" width="324" height="63" rx="18" fill="#2d6f7e"/><text x="480" y="339" fill="white" font-size="20" font-weight="700">Skillz</text><text x="480" y="361" fill="white" font-size="15">Shared skills for all three regions</text></g></svg>`;
    $('#universe-list').innerHTML = all.map(item => `<article class="universe-item${item.shared ? ' shared' : ''}"><strong>${/^https:\/\//.test(item.url) ? `<a href="${esc(item.url)}" target="_blank" rel="noopener noreferrer">${esc(item.name)}</a>` : esc(item.name)}</strong><br><small>${esc(item.role)}${item.shared ? ' · Shared across all three' : ''}</small></article>`).join('');
  }
  function renderCurrent() { const p = state.current; if (!p) return; $('#empty-state').hidden = true; $('#editor').hidden = false; fields.forEach(f => { const input = $(`#project-form [name="${f}"]`); if (input) input.value = p[f] || ''; }); $('#project-kind').textContent = kinds[p.kind] || p.kind; $('#project-title').textContent = p.name || 'Untitled'; $('#project-meta').textContent = `Revision ${p.revision ?? 0} · Last saved ${p.updatedAt ? new Date(p.updatedAt).toLocaleString() : 'locally pending'}`; $('#archive-button').textContent = p.status === 'archived' ? 'Restore draft' : 'Archive'; renderComponents(); renderTests(); renderSkills(); renderUniverse(); loadHistory(); }
  async function loadHistory() {
    const id = state.current?.id, token = ++state.historyToken;
    if (!id) return;
    $('#history').textContent = 'Loading revision history…';
    try {
      const data = await (await api(`/api/projects/${encodeURIComponent(id)}/history`)).json();
      if (token !== state.historyToken || id !== state.current?.id) return;
      $('#history').innerHTML = data.history.map(h => {
        const label = h.baseline ? ' · current-state baseline' : '';
        const action = h.restorable && h.revision !== state.current.revision
          ? `<button type="button" class="button secondary history-restore" data-revision="${esc(h.revision)}">Restore this version</button>`
          : '';
        return `<li><strong>r${esc(h.revision)}</strong> · ${esc(h.action)}${label}<br><small>${esc(h.summary)} · ${esc(new Date(h.at).toLocaleString())}</small>${action}</li>`;
      }).join('');
      $$('.history-restore').forEach(button => button.addEventListener('click', () => requestRestoreRevision(Number(button.dataset.revision))));
    } catch (_) {
      if (token === state.historyToken) $('#history').textContent = 'Revision history is unavailable right now.';
    }
  }
  function markDirty() { if (state.busy) return; state.dirty = true; state.validation = null; $('#save-button').textContent = 'Save draft · changes'; $('#project-title').textContent = $('#project-form [name="name"]').value || 'Untitled'; $('#validation-result').innerHTML = '<p>Edits are unsaved. Current review results are no longer shown. Save before checking readiness.</p>'; }
  function collect() { const p = { revision: state.current.revision, status: state.current.status || 'draft', components: state.current.components || [], tests: state.current.tests || [], skillIds: state.current.skillIds || [] }; fields.forEach(f => { p[f] = $(`#project-form [name="${f}"]`).value; }); return p; }
  async function refreshProjects() { const d = await (await api('/api/projects')).json(); state.projects = d.projects || []; renderLibrary(); }
  function showNew() {
    if (state.busy) return;
    const open = () => { if (state.saved) showSaved(structuredClone(state.saved)); $('#template-dialog').showModal(); };
    if (state.dirty) { state.pending = open; $('#confirm-dialog').showModal(); }
    else open();
  }
  async function createFromTemplate(id) {
    if (state.busy) return;
    const item = state.bootstrap.templates.find(t => t.id === id);
    if (!item) return;
    $('#template-dialog').close();
    setBusy(true);
    try {
      const project = await (await api('/api/projects', {method:'POST', body:JSON.stringify(item.project)})).json();
      showSaved(project); activatePanel('brief');
      status('Draft created. Adapt the starting instructions and save the specification before recording evidence.');
      await refreshAfterSave();
    } catch (error) { status(error.message, true); }
    finally { setBusy(false); }
  }
  async function save() {
    if (!state.current || state.busy) return false;
    const id = state.current.id, payload = collect();
    const previous = payload.tests.filter(t => t.status !== 'not-run' || t.actual);
    setBusy(true); clearStatus();
    try {
      const project = await (await api(`/api/projects/${id}`, {method:'PUT', body:JSON.stringify(payload)})).json();
      const reset = previous.some(old => project.tests.some(t => t.id === old.id && t.status === 'not-run' && !t.actual));
      showSaved(project);
      status(reset ? 'Saved. Changed specifications or acceptance criteria reset the old evidence. Record the new test run next.' : 'Saved locally.');
      await refreshAfterSave();
      return true;
    } catch (error) { status(error.message, true); return false; }
    finally { setBusy(false); }
  }
  async function requestOpen(id) {
    if (state.busy || state.current?.id === id) return;
    if (state.dirty) { state.pending = () => openProject(id); $('#confirm-dialog').showModal(); }
    else await openProject(id);
  }
  async function openProject(id) {
    if (state.busy) return;
    setBusy(true);
    try { showSaved(await (await api(`/api/projects/${encodeURIComponent(id)}`)).json()); clearStatus(); }
    catch (error) { status(error.message, true); }
    finally { setBusy(false); }
  }
  async function toggleArchive() {
    if (state.busy || !state.current || (state.dirty && !(await save()))) return;
    const id = state.current.id, payload = collect();
    payload.status = payload.status === 'archived' ? 'draft' : 'archived';
    setBusy(true);
    try {
      const project = await (await api(`/api/projects/${id}`, {method:'PUT', body:JSON.stringify(payload)})).json();
      showSaved(project);
      status(project.status === 'archived' ? 'Archived. Restore it whenever you need it again.' : 'Restored to the active library.');
      await refreshAfterSave();
    } catch (error) { status(error.message, true); }
    finally { setBusy(false); }
  }
  async function duplicateProject() {
    if (state.busy || !state.current) return;
    if (state.dirty && !(await save())) return;
    setBusy(true);
    try {
      const project = await (await api(`/api/projects/${state.current.id}/duplicate`, {method:'POST', body:JSON.stringify({revision: state.current.revision})})).json();
      showSaved(project);
      status('Duplicated as a fresh draft. Its acceptance evidence needs a new test run.');
      await refreshAfterSave();
    } catch (error) { status(error.message, true); }
    finally { setBusy(false); }
  }
  function requestRestoreRevision(revision) {
    if (state.busy || !state.current || !Number.isInteger(revision)) return;
    state.pendingRevision = revision;
    $('#revision-restore-dialog').showModal();
  }
  async function restoreRevision() {
    const sourceRevision = state.pendingRevision;
    state.pendingRevision = null;
    if (state.busy || !state.current || !Number.isInteger(sourceRevision)) return;
    if (state.dirty && !(await save())) return;
    const id = state.current.id;
    setBusy(true);
    try {
      const project = await (await api(`/api/projects/${encodeURIComponent(id)}/restore`, {
        method: 'POST',
        body: JSON.stringify({sourceRevision, currentRevision: state.current.revision}),
      })).json();
      showSaved(project);
      status(`Restored revision ${sourceRevision} as a new draft revision. Record fresh evidence before review.`);
      await refreshAfterSave();
    } catch (error) { status(error.message, true); }
    finally { setBusy(false); }
  }
  function requestDelete() {
    if (state.busy || !state.current) return;
    $('#delete-dialog').showModal();
  }
  async function deleteProject() {
    if (state.busy || !state.current) return;
    const id = state.current.id, revision = state.current.revision;
    setBusy(true);
    try {
      await api(`/api/projects/${id}`, {method:'DELETE', body:JSON.stringify({confirm:true, revision})});
      state.current = null; state.saved = null; state.dirty = false;
      $('#editor').hidden = true; $('#empty-state').hidden = false;
      await refreshProjects();
      status('Project deleted. Other local projects and backups were not changed.');
    } catch (error) { status(error.message, true); }
    finally { setBusy(false); }
  }
  async function validate() {
    if (state.busy || !state.current || (state.dirty && !(await save()))) return;
    setBusy(true);
    try {
      const data = await (await api(`/api/projects/${state.current.id}/validation`)).json();
      state.validation = data;
      $('#validation-result').innerHTML = `<p><strong>${data.readyForReview ? 'Ready for review' : 'Still shaping'}</strong> · ${esc(data.summary)}</p>${data.checks.map(c => `<div class="check ${esc(c.status)}"><span class="check-icon" aria-hidden="true">${c.status === 'pass' ? '✓' : c.status === 'fail' ? '×' : '!'}</span><div><strong>${esc(c.label)} · ${esc(c.status)}</strong><br><small>${esc(c.detail)}</small></div></div>`).join('')}`;
      status('Review checks reflect the saved revision and the evidence you recorded.');
    } catch (error) { status(error.message, true); }
    finally { setBusy(false); }
  }
  async function inspectPackage() {
    if (state.busy || !state.current || (state.dirty && !(await save()))) return;
    setBusy(true);
    try {
      const data = await (await api(`/api/projects/${state.current.id}/package`)).json();
      const wrap = $('#package-inspection');
      wrap.innerHTML = `<div class="inspection-heading"><div><p class="eyebrow">Generated, not certified</p><h3>Package inspection</h3></div><p class="muted">${esc(data.files.length)} files · manifest v${esc(data.manifest.manifestVersion)} · ${data.manifest.readyForReview ? 'review checks pass' : 'review checks incomplete'}</p></div><p class="muted">These are the exact text files prepared for the ZIP export. Inspect them before downloading; generated structure does not prove behavior or publication readiness.</p>${data.files.map(file => `<details class="package-file"><summary><strong>${esc(file.name)}</strong><span>${esc(file.size)} bytes</span></summary><pre>${esc(file.content)}</pre></details>`).join('')}`;
      wrap.hidden = false;
      status('Package inspected from the saved revision. ZIP export uses the same files.');
    } catch (error) { status(error.message, true); }
    finally { setBusy(false); }
  }
  async function download(format) {
    if (state.busy || !state.current || (state.dirty && !(await save()))) return;
    setBusy(true);
    try {
      const response = await api(`/api/projects/${state.current.id}/export?format=${encodeURIComponent(format)}`);
      const url = URL.createObjectURL(await response.blob()), link = document.createElement('a');
      link.href = url;
      link.download = `${state.current.name.replace(/[^a-z0-9]+/gi,'-').replace(/^-|-$/g,'') || 'foundry-draft'}.${format === 'markdown' ? 'md' : format}`;
      document.body.append(link); link.click(); link.remove();
      setTimeout(() => URL.revokeObjectURL(url), 1000);
      status(`${format.toUpperCase()} download prepared from the saved revision.`);
    } catch (error) { status(error.message, true); }
    finally { setBusy(false); }
  }
  async function backupWorkspace() {
    if (state.busy || (state.dirty && !(await save()))) return;
    setBusy(true);
    try {
      const response = await api('/api/workspace/backup');
      const url = URL.createObjectURL(await response.blob()), link = document.createElement('a');
      link.href = url; link.download = 'glee-fully-foundry-workspace.json'; document.body.append(link); link.click(); link.remove();
      setTimeout(() => URL.revokeObjectURL(url), 1000);
      status('Workspace backup prepared from all saved local projects and revision trails.');
    } catch (error) { status(error.message, true); }
    finally { setBusy(false); }
  }
  function importWorkspace(file) {
    if (!file || state.busy) return;
    state.pendingRestoreFile = file;
    $('#restore-dialog').showModal();
  }
  async function restoreWorkspace() {
    const file = state.pendingRestoreFile;
    state.pendingRestoreFile = null;
    if (!file || state.busy) return;
    setBusy(true);
    try {
      if (file.size > 10 * 1024 * 1024) throw new Error('Choose a workspace backup no larger than 10 MB.');
      const backup = JSON.parse(await file.text());
      await api('/api/workspace/restore', {method:'POST', body:JSON.stringify({backup, confirm:true, mode:'replace'})});
      state.current = null; state.saved = null; state.dirty = false;
      $('#editor').hidden = true; $('#empty-state').hidden = false;
      await refreshProjects();
      status('Workspace restored after complete validation. Current projects and revision trails now match the backup.');
    } catch (error) { status(error.message || 'The workspace backup is not valid.', true); }
    finally { $('#restore-file').value = ''; setBusy(false); }
  }
  async function openSource(id) {
    const token = ++state.sourceToken, projectId = state.current?.id;
    try {
      const source = await (await api(`/api/sources/${encodeURIComponent(id)}`)).json();
      if (token !== state.sourceToken || projectId !== state.current?.id) return;
      $('#source-title').textContent = source.title;
      $('#source-content').textContent = source.content;
      $('#source-viewer').hidden = false;
      $('#source-title').setAttribute('tabindex', '-1'); $('#source-title').focus();
      $('#source-viewer').scrollIntoView({block:'start'});
    } catch (error) { if (token === state.sourceToken) status(error.message, true); }
  }
  async function importFile(file) {
    if (!file || state.busy) return;
    if (state.dirty) { state.pending = () => importFileAfterWarning(file); $('#confirm-dialog').showModal(); }
    else await importFileAfterWarning(file);
  }
  async function importFileAfterWarning(file) {
    if (state.busy) return;
    setBusy(true);
    try {
      if (file.size > 1024 * 1024) throw new Error('Choose a project JSON file smaller than 1 MB.');
      const imported = JSON.parse(await file.text());
      const project = await (await api('/api/import', {method:'POST', body:JSON.stringify({project: imported.project || imported})})).json();
      showSaved(project); activatePanel('brief');
      status('Imported as a fresh draft. Its acceptance cases need a new test run.');
      await refreshAfterSave();
    } catch (error) { status(error.message || 'The file is not valid project JSON.', true); }
    finally { $('#import-file').value = ''; setBusy(false); }
  }
  function activatePanel(name) { $$('.editor-tab').forEach(b => { const active = b.dataset.panel === name; b.classList.toggle('active', active); if (active) b.setAttribute('aria-current', 'page'); else b.removeAttribute('aria-current'); }); $$('.panel').forEach(p => p.classList.toggle('active',p.id === `panel-${name}`)); }
  function applyTheme() {
    let theme = 'light';
    try { theme = localStorage.getItem('foundry-theme') === 'dark' ? 'dark' : 'light'; } catch (_) {}
    document.documentElement.dataset.theme = theme;
    const button = $('#theme-button');
    button.textContent = theme === 'dark' ? 'Day mode' : 'Night mode';
    button.setAttribute('aria-pressed', String(theme === 'dark'));
  }
  function toggleTheme() {
    const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = next;
    try { localStorage.setItem('foundry-theme', next); } catch (_) {}
    const button = $('#theme-button');
    button.textContent = next === 'dark' ? 'Day mode' : 'Night mode';
    button.setAttribute('aria-pressed', String(next === 'dark'));
  }
  async function init() { $('#new-button').addEventListener('click',showNew); $('#import-button').addEventListener('click',() => $('#import-file').click()); $('#import-file').addEventListener('change',e => importFile(e.target.files[0])); $('#backup-button').addEventListener('click',backupWorkspace); $('#restore-button').addEventListener('click',() => $('#restore-file').click()); $('#restore-file').addEventListener('change',e => importWorkspace(e.target.files[0])); $('#theme-button').addEventListener('click',toggleTheme); $('#project-search').addEventListener('input',renderLibrary); $$('.tab').forEach(b => b.addEventListener('click',() => { state.library=b.dataset.library; $$('.tab').forEach(x => {x.classList.toggle('active',x===b);x.setAttribute('aria-selected',x===b);});renderLibrary(); })); $$('.editor-tab').forEach(b => b.addEventListener('click',()=>activatePanel(b.dataset.panel))); $('#project-form').addEventListener('submit',e => e.preventDefault()); $('#project-form').addEventListener('input',markDirty); $('#project-form').addEventListener('change',markDirty); $('#save-button').addEventListener('click',save); $('#duplicate-button').addEventListener('click',duplicateProject); $('#archive-button').addEventListener('click',toggleArchive); $('#delete-button').addEventListener('click',requestDelete); $('#validate-button').addEventListener('click',validate); $('#inspect-button').addEventListener('click',inspectPackage); $$('[data-export]').forEach(b => b.addEventListener('click',() => download(b.dataset.export))); $('#add-component').addEventListener('click',()=>{state.current.components.push({id:safeId(),name:'',purpose:'',dependsOn:[]});markDirty();renderComponents();}); $('#add-test').addEventListener('click',()=>{state.current.tests.push({id:safeId(),name:'',expected:'',actual:'',status:'not-run'});markDirty();renderTests();}); $('#close-source').addEventListener('click',()=>{ state.sourceToken++; $('#source-viewer').hidden=true; }); $('#confirm-dialog').addEventListener('close',()=>{if($('#confirm-dialog').returnValue==='leave'&&state.pending){const fn=state.pending;state.pending=null;fn();}else state.pending=null;}); $('#delete-dialog').addEventListener('close',()=>{if($('#delete-dialog').returnValue==='delete')deleteProject();}); $('#restore-dialog').addEventListener('close',()=>{if($('#restore-dialog').returnValue==='restore')restoreWorkspace();else state.pendingRestoreFile=null;}); $('#revision-restore-dialog').addEventListener('close',()=>{if($('#revision-restore-dialog').returnValue==='restore')restoreRevision();else state.pendingRevision=null;}); applyTheme(); window.addEventListener('beforeunload',e=>{if(state.dirty){e.preventDefault();e.returnValue='';}});
    try { const [boot, projects] = await Promise.all([api('/api/bootstrap'),api('/api/projects')]); state.bootstrap = await boot.json(); state.projects = (await projects.json()).projects || []; setConnection(true); renderTemplates(); renderLibrary(); renderUniverse(); } catch(e) { setConnection(false); $('#empty-state').querySelector('p:last-of-type').textContent = 'The local service is not running yet. Start it, then refresh this workspace.'; status(e.message,true); }
  }
  init();
})();
