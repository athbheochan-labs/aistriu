<section class="content" aria-labelledby="about-title">
  <p class="eyebrow">About</p>
  <h1 id="about-title">Built for the Aistriu project.</h1>
  <p>
    This route is part of the initial SvelteKit structure and gives the app a
    place for product, team, or project context as the frontend grows.
  </p>
</section>

<style>
  .content {
    margin: 0 auto;
    max-width: 46rem;
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
    font-size: clamp(2.25rem, 6vw, 4rem);
    line-height: 1;
    margin: 0;
  }

  p {
    color: var(--al-colour-ink-muted);
    font-size: 1.1rem;
    line-height: 1.7;
    margin-top: var(--al-space-6);
  }
</style>
