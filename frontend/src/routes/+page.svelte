<section class="hero" aria-labelledby="home-title">
  <div>
    <p class="eyebrow">Athbheochan Labs</p>
    <h1 id="home-title">Aistriu</h1>
    <p class="lede">
      A SvelteKit frontend ready to connect with the FastAPI backend.
    </p>
  </div>

  <div class="status-panel" aria-label="Project setup status">
    <h2>Project Setup</h2>
    <ul>
      <li>TypeScript enabled</li>
      <li>Basic routes in place</li>
      <li>Brand tokens loaded globally</li>
    </ul>
  </div>
</section>

<style>
  .hero {
    align-items: center;
    display: grid;
    gap: var(--al-space-12);
    grid-template-columns: minmax(0, 1fr) minmax(18rem, 26rem);
    margin: 0 auto;
    max-width: 72rem;
  }

  .eyebrow {
    color: var(--al-colour-forest);
    font-weight: 750;
    letter-spacing: 0.08em;
    margin: 0 0 var(--al-space-3);
    text-transform: uppercase;
  }

  h1 {
    font-family: var(--al-font-display);
    font-size: clamp(3rem, 8vw, 6rem);
    line-height: 0.95;
    margin: 0;
  }

  .lede {
    color: var(--al-colour-ink-muted);
    font-size: 1.2rem;
    line-height: 1.6;
    margin: var(--al-space-6) 0 0;
    max-width: 38rem;
  }

  .status-panel {
    background: var(--al-colour-surface-raised);
    border: 1px solid var(--al-colour-line);
    border-radius: var(--al-radius-lg);
    box-shadow: var(--al-shadow-md);
    padding: var(--al-space-6);
  }

  .status-panel h2 {
    font-family: var(--al-font-display);
    font-size: 1.5rem;
    margin: 0 0 var(--al-space-4);
  }

  ul {
    display: grid;
    gap: var(--al-space-3);
    list-style: none;
    margin: 0;
    padding: 0;
  }

  li {
    border-left: 4px solid var(--al-colour-mint);
    color: var(--al-colour-ink-muted);
    padding-left: var(--al-space-3);
  }

  @media (max-width: 760px) {
    .hero {
      grid-template-columns: 1fr;
    }
  }
</style>
