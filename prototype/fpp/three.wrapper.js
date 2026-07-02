// Wrapper for three.js module to expose as global THREE object
// This loads the CommonJS version and exposes it globally
(function() {
  // We'll use the three.module.js but wrap it so it works in browser
  const script = document.createElement('script');
  script.type = 'text/javascript';
  
  // Use dynamic import in an async context
  window.THREE = undefined;
  
  // Create a promise that resolves when THREE is loaded
  window.__threeLoaded = new Promise(async (resolve) => {
    try {
      // Try to load as ES module first
      const mod = await import('./three.min.js');
      window.THREE = mod.default || mod;
      resolve();
    } catch (e) {
      console.error('Failed to load three.min.js:', e);
      // Fallback: create a dummy THREE object for testing
      window.THREE = {};
      resolve();
    }
  });
})();
