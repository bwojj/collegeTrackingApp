const modalContainer = document.querySelector('.modal-container');
const customModalContainer = document.querySelector('.modal-2');
const overlay = document.querySelector('.overlay');
const fullOverlay = document.querySelector('.fullOverlay');

const search = document.getElementById('search-food');

function macroUpdate(circle, current, goal, percentageText){
    let targetProgress = (current / goal) * 100;
    let progress = 0;


    const interval = setInterval(() => {
        if (progress >= targetProgress){
            clearInterval(interval);
            return;
        }
        progress += 1;
        const offset = 188.5 - (188.5 * progress) / 100;
        circle.style.strokeDashoffset = offset;
        percentageText.textContent = `${progress}%`
    }, 60);
}

function progressAnimation(){
    const progressCircle = document.querySelectorAll('.circle-progress');
    const percentageText = document.querySelectorAll('.percentage');

    const goals = [170, 250, 70]

    const currents = [
        parseFloat(document.getElementById('proteinG').textContent),
        parseFloat(document.getElementById('carbsG').textContent),
        parseFloat(document.getElementById('fatG').textContent)
    ]

    for (let i = 0; i < progressCircle.length; i++){
        macroUpdate(progressCircle[i], currents[i], goals[i], percentageText[i])
    }
}

const modalOpen = () => {
    modalContainer.classList.add('active');
    overlay.classList.add('active');
}

const modalClose = () => {
    modalContainer.classList.remove('active');
    overlay.classList.remove('active');

    modalContainer.classList.add('closing');

    setTimeout(() => {
        modalContainer.classList.remove('closing');
    }, 300); 
}

const customModalOpen = () => {
    customModalContainer.classList.add('active');
    fullOverlay.classList.add('active');
}

const customModalClose = () => {
    customModalContainer.classList.remove('active');
    fullOverlay.classList.remove('active');
    overlay.classList.remove('active');

    customModalContainer.classList.add('closing');

    setTimeout(() => {
        customModalContainer.classList.remove('closing');
    }, 300);
}

const foodChoice = () => {
    document.querySelectorAll('#food-list .row').forEach(row => {
        row.addEventListener('click', () => {
            let foodName = row.querySelector('p').textContent.trim();
            
            if (foodName != 'Custom Food'){
                document.getElementById("search-food").placeholder = foodName;
                document.getElementById("search-food").value = foodName;
            }
        })
    })
}

progressAnimation()
foodChoice()

search.addEventListener("keyup", function(){
    let filter = this.value.toLowerCase();
    let rows = document.querySelectorAll("#food-list .row");

    rows.forEach(row => {
        let text = row.textContent.toLowerCase();
        if (text.includes(filter)) {
            row.style.display = "";
        }
        else {
            row.style.display = "none";
        }
    });
});

document.addEventListener('keydown', (e) => {
    // Only react to arrow keys
    if (!["ArrowDown", "ArrowUp", "ArrowLeft", "ArrowRight"].includes(e.key)) return;

    // Get all inputs in order
    const inputs = Array.from(document.querySelectorAll('input'));
    const active = document.activeElement;
    const index = inputs.indexOf(active);

    if (index === -1) return; // not focused on an input

    // ↓ Go to next input
    if (e.key === "ArrowDown" || e.key === "ArrowRight") {
        const next = inputs[index + 1];
        if (next) {
            e.preventDefault();
            next.focus();
        }
    }

    // ↑ Go to previous input
    if (e.key === "ArrowUp" || e.key === "ArrowLeft") {
        const prev = inputs[index - 1];
        if (prev) {
            e.preventDefault();
            prev.focus();
        }
    }
});

