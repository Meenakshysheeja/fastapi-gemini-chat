async function sendToGemini() {
    const userInput = document.getElementById("userInput").value;
    const responseBox = document.getElementById("responseBox");

    // Show loading text & hide response box initially
    responseBox.style.display = "block";
    responseBox.innerText = "Loading...";

    try {
        const response = await fetch("http://localhost:8000/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt: userInput })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        responseBox.innerText = data.response;
    } catch (error) {
        responseBox.innerText = "Error: " + error.message;
        console.error("Request failed:", error);
    }
}

// Ensure the function is available globally
window.sendToGemini = sendToGemini;

