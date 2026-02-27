const micBtn = document.getElementById("micBtn");
const liveText = document.getElementById("liveText");
const statusDiv = document.getElementById("status");
const activityLog = document.getElementById("activityLog");

let recognition;

if ("webkitSpeechRecognition" in window) {
  recognition = new webkitSpeechRecognition();
  recognition.lang = "en-IN";
  recognition.continuous = false;

  recognition.onstart = () => {
    statusDiv.textContent = "🎧 Listening...";
    statusDiv.className = 'status listening';
    micBtn.classList.add('listening');
  };

  recognition.onresult = (event) => {
    const text = event.results[0][0].transcript;
    liveText.textContent = text;
    statusDiv.textContent = "✅ Processed";
    statusDiv.className = 'status processed';
    micBtn.classList.remove('listening');

    // add to activity log
    const li = document.createElement("li");
    li.textContent = `${new Date().toLocaleTimeString()} — ${text}`;
    activityLog.prepend(li);
  };

  recognition.onerror = () => {
    statusDiv.textContent = "⚠️ Error occurred. Please try again.";
    statusDiv.className = 'status error';
    micBtn.classList.remove('listening');
  };
}

micBtn.onclick = () => {
  if (recognition) {
    recognition.start();
  } else {
    alert("Speech Recognition not supported in this browser.");
  }
}; 