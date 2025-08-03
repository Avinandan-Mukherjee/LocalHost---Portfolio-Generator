const codeBtn = document.getElementById("codeBtn");
const previewBtn = document.getElementById("previewBtn");
const codeSection = document.getElementById("code-section");
const previewSection = document.getElementById("preview-section");
const iframe = document.getElementById("preview-frame");

codeBtn.onclick = () => {
    codeSection.style.display = "block";
    previewSection.style.display = "none";
    codeBtn.classList.add("active");
    previewBtn.classList.remove("active");
};

previewBtn.onclick = () => {
    codeSection.style.display = "none";
    previewSection.style.display = "flex";
    codeBtn.classList.remove("active");
    previewBtn.classList.add("active");
};

function openNewTab() {
    const url = iframe.src;
    window.open(url, '_blank');
}

function toggleMobile() {
    iframe.classList.toggle("mobile");
}


codeSection.style.display = "block";



function showFile(fileType) {
    // Hide 
    document.querySelectorAll('.code-file').forEach(file => {
        file.classList.remove('active');
    });
    
    // Remove 
    document.querySelectorAll('.file-tab').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Show 
    document.getElementById(fileType + '-file').classList.add('active');
    
    // Add 
    event.target.classList.add('active');
    
    setTimeout(() => {
        Prism.highlightAll();
    }, 100);
}

function copyCode(fileType) {
    const codeElement = document.querySelector(`#${fileType}-file pre code`);
    const textToCopy = codeElement.textContent;
    
    navigator.clipboard.writeText(textToCopy).then(function() {
        
        const copyBtn = event.target.closest('.copy-btn');
        const iconElement = copyBtn.querySelector('i');
      
        const originalIcon = iconElement.className;
        
        
        copyBtn.classList.add('copied');
        iconElement.className = 'fas fa-check';
        
        setTimeout(() => {
            copyBtn.classList.remove('copied');
            iconElement.className = originalIcon;
        }, 3000);
    }).catch(function(err) {
        console.error('Could not copy text: ', err);
    });
}




document.addEventListener('DOMContentLoaded', function() {
    setTimeout(() => {
        Prism.highlightAll();
    }, 200);
});