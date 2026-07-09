const chatToggle=document.getElementById("chatToggle");

const chatBox=document.getElementById("chatBox");

const closeChat=document.getElementById("closeChat");

chatToggle.onclick=()=>{

    chatBox.style.display="flex";

}

closeChat.onclick=()=>{

    chatBox.style.display="none";

}

const sendBtn=document.getElementById("sendBtn");

sendBtn.onclick=async()=>{

    const question=document.getElementById("question").value;

    const chatBody=document.getElementById("chatBody");

    if(question==="") return;

    chatBody.innerHTML+=`
        <div class="user-message">
            ${question}
        </div>
    `;

    document.getElementById("question").value="";

    const response=await fetch("/api/ai/chat/",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            question:question

        })

    });

    const data=await response.json();

    chatBody.innerHTML+=`
        <div class="bot-message">
            ${data.answer}
        </div>
    `;

    chatBody.scrollTop=chatBody.scrollHeight;

}