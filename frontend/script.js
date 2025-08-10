document.getElementById('loginForm').onsubmit = async e => {
  e.preventDefault();
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  try {
    const res = await fetch('http://13.60.203.183:5000/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });
    const data = await res.json();
    if (data.success) {
      window.location.href = 'home.html';
    } else {
      document.getElementById('errorMsg').innerText = 'Invalid credentials.';
    }
  } catch {
    document.getElementById('errorMsg').innerText = 'Unable to reach server.';
  }
};

