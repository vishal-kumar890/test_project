


function get_answer(operator){
    console.log('operator',operator)
    let first_num = document.getElementById('first_num').value
    let second_num = document.getElementById('second_num').value

    if (first_num.trim() ==  "" || second_num.trim() == ""){
        alert('Please ensure that you enter value in both fields')
    }

    postData(`/${operator}`,{first_num:first_num,second_num:second_num}).then(data=>{
        console.log('data',data)
        document.getElementById('output_text').innerText = data

        document.getElementById('output_div').style.display = ""
    })
}


async function postData(url = '', data = {}) {
    const response = await fetch(url, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'include', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json',
        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    if (response.status == 200) {
        if (response.headers.get('Content-Type') == 'application/json') {
            return response.json(); // parses JSON response into native JavaScript objects
        } else {
            console.log('content type not application/json')

        }
    }else if (response.status == 401) {
        window.location.href = "/home";
    }else {
        let val = await response.text()
        // confirmBox("Error!", val)
        confirmBox("Oops!", val)
        document.querySelectorAll('.modal-preloader').forEach(a=>a.style.display = "none");
        return Promise.reject(new Error(val))
    }
}

document.getElementById('addition').onclick = get_answer.bind(null,'sum')
document.getElementById('multiplication').onclick = get_answer.bind(null,'multiply')
document.getElementById('subtraction').onclick = get_answer.bind(null,'subtract')