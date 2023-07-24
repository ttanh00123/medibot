function sendMessage() {
    const messageInput = document.getElementById("messageInput");
    const message = messageInput.value.trim();
    if (message === "") return;

    const chatMessages = document.getElementById("chatMessages");
    const messageBubble = document.createElement("div");
    messageBubble.className = "message-bubble";
    messageBubble.innerText = message;

    chatMessages.appendChild(messageBubble);
    messageInput.value = "";
    chatMessages.scrollTop = chatMessages.scrollHeight;
}s