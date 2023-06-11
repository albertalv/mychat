async () => {
    try {
      const response = await fetch('/room/');
      const data = await response.text();
      document.getElementById("contenedor").innerHTML = data;
    } catch (error) {
      console.error("Error:", error);
    }
}