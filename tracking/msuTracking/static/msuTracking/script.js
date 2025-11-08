const modalContainer = document.querySelector('.modal-container');
const overlay = document.querySelector('.overlay');

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
}

const foodChoice = () => {
    document.querySelectorAll('#food-list .row').forEach(row => {
        row.addEventListener('click', () => {
            let foodName = row.querySelector('p').textContent.trim();
            
            document.getElementById("search-food").placeholder = foodName;
            document.getElementById("search-food").value = foodName;
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
