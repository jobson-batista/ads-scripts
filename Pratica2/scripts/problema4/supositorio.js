let sleep = time => new Promise(resolve => {
    setTimeout(resolve, time);
})

let download = (filename, text) => {
    let element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);
    element.style.display = 'none';
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
}

let main = async() => {
    results = [['Lambda Time-Spent\n']]
    for(let i = 1; i <= 8; i++){
        temp = []
        document.querySelector('input#Lambda').setAttribute('value', i);
        document.querySelector('input#Mu').setAttribute('value', 1/0.84);
        document.querySelector('input#c').setAttribute('value', 8);
        document.getElementById('calculate').click();
        await sleep(5000);
        
        temp.push(document.getElementById('Lambda').value);
        temp.push(document.getElementById('WValue').textContent.split(' ')[0]);
        results.push(temp.toString().split(',').join(' ')+"\n");
    }
    console.log(results);
    download("results-4.txt",results.toString().split(','));
}

main();