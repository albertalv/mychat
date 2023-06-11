document.getElementById("botonSiete").addEventListener("click", async () => {
    try {
      const response = await fetch('/validacion/');
      const data = await response.text();
      document.getElementById("contenedor").innerHTML = data;
    } catch (error) {
      console.error("Error:", error);
    }
  });

  document.getElementById("botonOcho").addEventListener("click", async () => {
    try {
      const response = await fetch('/resolverDenuncia/');
      const data = await response.text();
      document.getElementById("contenedor").innerHTML = data;
    } catch (error) {
      console.error("Error:", error);
    }
  });

  document.getElementById("botonNueve").addEventListener("click", async () => {
    try {
      const response = await fetch('/crearCategoria/');
      const data = await response.text();
      document.getElementById("contenedor").innerHTML = data;
    } catch (error) {
      console.error("Error:", error);
    }
  });