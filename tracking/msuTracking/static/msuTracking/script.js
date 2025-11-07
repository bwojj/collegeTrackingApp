const modalContainer = document.querySelector('.modal-container');
const overlay = document.querySelector('.overlay');

const search = document.getElementById('search-food');

function progressAnimation(){
    let progress = 0; 

    const progressCircle = document.querySelectorAll('.circle-progress');
    const percentageText = document.querySelectorAll('.percentage');

    const interval = setInterval(() => {
        
    if (progress < 100) {
        progress += 1;
        const offset = 339.292 - (339.292 * progress) / 100;
        for (let i = 0; i < progressCircle.length; i++){
            progressCircle[i].style.strokeDashoffset = offset;
            percentageText[i].textContent = `${progress}%`
        }
    }
    else {
        clearInterval(interval);
    }
}, 60);
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
