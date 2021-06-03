let sleep = time => new Promise(resolve => {
    setTimeout(resolve, time);
})

// Para gerar um txt para download.
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
    results = [['C Time-Spent\n']]
    for(let i = 8; i <= 25; i++){
        temp = []
        document.querySelector('input#Lambda').setAttribute('value', 9.5);
        document.querySelector('input#Mu').setAttribute('value', 1/0.84);
        document.querySelector('input#c').setAttribute('value', i);
        document.getElementById('calculate').click();
        await sleep(5000);
        
        temp.push(document.getElementById('c').value);
        temp.push(document.getElementById('WValue').textContent.split(' ')[0]);
        results.push(temp.toString().split(',').join(' ')+"\n");
    }
    console.log(results);
    download("results.txt",results.toString().split(','));
}

main();