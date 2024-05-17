
const common_instruction = document.querySelector('#common_instruction')

const tests_by_price = document.querySelector('#tests_by_price')

const tests_in_categories = document.querySelector('#tests_in_categories')

let label = ""
let datalabels = []
let datadata = []

if (common_instruction != null){
    label = "Instructions"
    const data = JSON.parse(common_instruction.innerText)
    
    for(var key in data){
        if (data.hasOwnProperty(key)){
            datalabels.push(key)
            datadata.push(data[key])            
        }
    }
}

if (tests_in_categories != null){
    label = "Categories"
    const data = JSON.parse(tests_in_categories.innerText)
    
    for(var key in data){
        if (data.hasOwnProperty(key)){
            datalabels.push(key)
            datadata.push(data[key])            
        }
    }
}

if (tests_by_price != null){
    label = "Prices"
    const data = JSON.parse(tests_by_price.innerText)
    
    for(var key in data){
        if (data.hasOwnProperty(key)){
            datalabels.push(key)
            datadata.push(data[key])            
        }
    }
}


const canvas = document.getElementById('myChart');
      
new Chart(canvas, {
    type: 'doughnut',
    data:  {
        labels: datalabels,
        datasets: [{
            label: label,
            data: datadata,
            borderWidth: 1
        }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: `${label} Doughnut Chart`
        }
      }
    },
});