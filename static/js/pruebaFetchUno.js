
document.getElementById("boton").addEventListener("click", async () => {
    try {
      const response = await fetch('/contenido/');
      const data = await response.text();
      document.getElementById("contenedor").innerHTML = data;
    } catch (error) {
      console.error("Error:", error);
    }
  });
  
 /* document.getElementById("botonDos").addEventListener("click", async () => {
    try {
      const response = await fetch('/contenidoDos/');
      const data = await response.text();
      document.getElementById("contenedor").innerHTML = data;
    } catch (error) {
      console.error("Error:", error);
    }
  });*/
  
  document.getElementById("botonTres").addEventListener("click", async () => {
    try {
      const response = await fetch('/crud_user');
      const data = await response.text();
      document.getElementById("contenedor").innerHTML = data;
    } catch (error) {
      console.error("Error:", error);
    }
  });
  
  document.getElementById("botonCuatro").addEventListener("click", async () => {
    try {
      const response = await fetch('/my_tokens/');
      const data = await response.text();
      document.getElementById("contenedor").innerHTML = data;
    } catch (error) {
      console.error("Error:", error);
    }
  });
  
  document.getElementById("botonCinco").addEventListener("click", async () => {
    try {
      const response = await fetch('/my_money/');
      const data = await response.text();
      document.getElementById("contenedor").innerHTML = data;
    } catch (error) {
      console.error("Error:", error);
    }
  });
  
  document.getElementById("botonSeis").addEventListener("click", async () => {
    try {
      const response = await fetch('/buzon/');
      const data = await response.text();
      document.getElementById("contenedor").innerHTML = data;
    } catch (error) {
      console.error("Error:", error);
    }
  });
  
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
 /* document.getElementById("botonDos").addEventListener("click", async () => {
    try {
      const response = await fetch('/lobby');
      const data = await response.text();
      document.getElementById("contenedor").innerHTML = data;
    } catch (error) {
      console.error("Error:", error);
    }
  });*/
  