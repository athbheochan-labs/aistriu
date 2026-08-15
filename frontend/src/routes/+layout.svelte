<script lang="ts">
  import '$lib/styles/tokens.css';

  let { children } = $props();
</script>

<svelte:head>
  <title>Aistriu | Athbheochan Labs</title>
  <meta
    name="description"
    content="Aistriu by Athbheochan Labs."
  />
</svelte:head>

<div class="shell">
  <header class="site-header">
    <a class="brand" href="/" aria-label="Aistriu home">
      <span class="brand-mark" aria-hidden="true">A</span>
      <span>
        <strong>Aistriu</strong>
        <small>Athbheochan Labs</small>
      </span>
    </a>

    <nav aria-label="Main navigation">
      <a href="/">Home</a>
      <a href="/about">About</a>
    </nav>
  </header>

  <main>
    {@render children()}
  </main>
</div>

<style>
  .shell {
    min-height: 100vh;
  }

  .site-header {
    align-items: center;
    border-bottom: 1px solid var(--al-colour-line);
    display: flex;
    gap: var(--al-space-6);
    justify-content: space-between;
    padding: var(--al-space-4) clamp(var(--al-space-4), 4vw, var(--al-space-12));
  }

  .brand {
    align-items: center;
    display: inline-flex;
    gap: var(--al-space-3);
    text-decoration: none;
  }

  .brand-mark {
    align-items: center;
    background: var(--al-colour-forest);
    border-radius: var(--al-radius-md);
    color: white;
    display: inline-flex;
    font-family: var(--al-font-display);
    font-size: 1.25rem;
    height: 2.5rem;
    justify-content: center;
    width: 2.5rem;
  }

  .brand strong,
  .brand small {
    display: block;
  }

  .brand strong {
    font-family: var(--al-font-display);
    font-size: 1.15rem;
  }

  .brand small {
    color: var(--al-colour-ink-muted);
    font-size: 0.8rem;
  }

  nav {
    display: flex;
    gap: var(--al-space-4);
  }

  nav a {
    color: var(--al-colour-ink-muted);
    font-size: 0.95rem;
    font-weight: 650;
    text-decoration: none;
  }

  nav a:hover {
    color: var(--al-colour-forest);
  }

  main {
    padding: clamp(var(--al-space-8), 6vw, var(--al-space-16))
      clamp(var(--al-space-4), 4vw, var(--al-space-12));
  }

  @media (max-width: 560px) {
    .site-header {
      align-items: flex-start;
      flex-direction: column;
    }
  }
</style>
