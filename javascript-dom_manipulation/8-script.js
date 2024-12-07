document.addEventListener("DOMContentLoaded", async function () {
    try {
      let response = await fetch("https://hellosalut.stefanbohacek.dev/?lang=fr");
      let data = await response.json();
      displayHello(data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  });
  
  function displayHello(data) {
    let container = document.getElementById("hello");
    container.textContent = data.hello;
  }
  