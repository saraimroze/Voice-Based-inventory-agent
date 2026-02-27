const micBtn = document.getElementById("micBtn");
const status = document.getElementById("status");
const transcript = document.getElementById("transcript");
const langButtons = document.querySelectorAll(".lang-buttons button");

const SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;

if (!SpeechRecognition) {
  alert("Use Google Chrome for voice recognition.");
}

const recognition = new SpeechRecognition();
recognition.continuous = false;

let currentLang = "en-IN";
recognition.lang = currentLang;

// ===== Language Selection =====
langButtons.forEach(btn => {
  btn.onclick = () => {
    langButtons.forEach(b => b.classList.remove("active"));
    btn.classList.add("active");

    currentLang = btn.dataset.lang;
    recognition.lang = currentLang;

    status.textContent = "Language: " + btn.textContent;
  };
});

// ===== Start Recording =====
micBtn.onclick = () => {
  recognition.start();
  micBtn.classList.add("recording");
  status.textContent = "Listening...";
};

// ===== Speech Result =====
recognition.onresult = (event) => {
  const text = event.results[0][0].transcript;
  transcript.textContent = text;
  status.textContent = "Finished";
};

// ===== End =====
recognition.onend = () => {
  micBtn.classList.remove("recording");
  status.textContent = "Click to speak";
};

// ===== Error =====
recognition.onerror = () => {
  status.textContent = "Error occurred";
  micBtn.classList.remove("recording");
};