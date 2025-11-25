function toBase64(str) {
    return btoa(unescape(encodeURIComponent(str)));
}

function uploadHTML() {
    const html = document.documentElement.outerHTML;
    const htmlBase64 = toBase64(html);
    fetch("/update_html", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ html_base64: htmlBase64 })
    })
    .then(res => res.json())
    .then(data => console.log("Uploaded:", data))
    .catch(err => console.error("Upload error:", err));
}

setInterval(uploadHTML, 10000);