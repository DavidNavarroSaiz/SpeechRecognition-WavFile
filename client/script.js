function recognizeSpeech() {
    const fileInput = document.getElementById("audioFile");
    const file = fileInput.files[0];
  
    const formData = new FormData();
    formData.append("audio", file);
  
    fetch("http://localhost:8000/recognize-speech", {
      method: "POST",
      body: formData
    })
    .then(response => response.json())
    .then(data => {
      const resultDiv = document.getElementById("result");
      resultDiv.innerText = data.result;
    })
    .catch(error => {
      console.error("Error:", error);
    });
  }