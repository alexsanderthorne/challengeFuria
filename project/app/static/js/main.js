function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();
    if (!message) return;
  
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div><strong>Você:</strong> ${message}</div>`;
  
    fetch("/chat", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({message})
    })
      .then(response => response.json())
      .then(data => {
        chatBox.innerHTML += `<div><strong>Pantera:</strong> ${data.response}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
      });
  
    input.value = "";
  }
  