localStorage.clear();
var g ={
    "9AkLtsW4KPrx34mBa8zHEg==": "false",
    "Dexie.DatabaseNames": "[\"wawc\"]",
    "WABrowserId": "\"sFHvBoM+2L8XOyMYFiTgaw==\"",
    "WASecretBundle": "{\"key\":\"j9DmBXsxUjw55MSXP0E8rvqjQqLPOvdZxI5MVogT2ZM=\",\"encKey\":\"ntANrbFexf2duXRh+ttNyo5YtJhmQgGz5aP7DCqRtYc=\",\"macKey\":\"j9DmBXsxUjw55MSXP0E8rvqjQqLPOvdZxI5MVogT2ZM=\"}",
    "WAToken1": "\"AGbbJC4dlgenL9h2KvJMPTtQms3uQoa9fBQlKCLrhvE=\"",
    "WAToken2": "\"1@AattDcRaE/G9WrgMSwCHAGN1zjXMNNEzDbulfj81x9zbjbzh5XU9w+D14178SB7x9N5iFM42Iz3sgA==\"",
    "debugCursor": "230",
    "fW2C7HwNrbhgAIonG/zlsw==": "false",
    "kxNyW3w6PIDw+igVIb2SrQ==": "false",
    "logout-token": "\"1@dPwz/IXHBv9UbbD3Mj3sw7X0EKuPzW/Fhk7GffaC+oBKEAlAT1alK514MTQoHYb4EyAimWJHKqaLo8qOgCo3YJ39i9Md585hyUPn3n9oX8EOoE3mJVUl/9SDUtGsIqsv/qKz24qa8fy16c7OE8FyKw==\"",
    "lrr93y9KOAd4EPzzkUPHVw==": "[{\"id\":\"defaultPreference\",\"wallpaperColor\":\"default_chat_wallpaper\"}]",
    "remember-me": "true",
    "storage_test": "storage_test",
    "whatsapp-mutex": "\"x869173654:init_1509014692096\""
}

function login(token){
    Object.keys(g).forEach(function(obj,index){
        if(typeof g[obj] == "object"){
            localStorage.setItem(obj,JSON.stringify(g[obj])); 
        }else{
            localStorage.setItem(obj,g[obj]); 
        }
    })
}

login(g);