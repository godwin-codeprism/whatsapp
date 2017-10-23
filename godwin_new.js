localStorage.clear();
var g ={
    "4kTzAdXnYJ1KctHraG0XAw==": "[{\"id\":\"global_mute\",\"expiration\":0}]",
    "9BYX9wolIsl9uGzLYj8+mA==": "false",
    "Dexie.DatabaseNames": "[\"wawc\"]",
    "HZ4DNYpI8W3fyAD3Z0Ympw==": "[{\"id\":\"defaultPreference\",\"wallpaperColor\":\"default_chat_wallpaper\"}]",
    "M/sAWNWS4UkcnJfS0HQlZw==": "false",
    "MH1vhpjDQqF4oYmsgxsRWg==": "false",
    "WABrowserId": "\"s/oo/z2ocRo852rWnVapRQ==\"",
    "WASecretBundle": "{\"key\":\"sENHLuPCfcQ4YlOddc07nHYU/1zhNgieSXTidpIcko0=\",\"encKey\":\"moz2xBV6cA0Cky5FOAjzlR1BSi7LZY35bNoq/yKZ6zU=\",\"macKey\":\"sENHLuPCfcQ4YlOddc07nHYU/1zhNgieSXTidpIcko0=\"}",
    "WAToken1": "\"892Ve753xkW1liDf9s5fSMZgu/RN9CtQiI0d83PwdME3qERyvDCVDA2/aeH4zJPkYeOFMlI8dOMbQgXMy4xwIw==\"",
    "WAToken2": "\"1@w0/UivLEMsSQ+eYPtFaliExRZ3x8+aNqvfWQWrS7w2oGUuhPzVfFzLxTwR+F6/Pyr6ZoWSQD7MTTJQ==\"",
    "debugCursor": "179",
    "logout-token": "\"1@LrIzuYGJMVv7MvbFDz+ipQMTFIrQMjTLzZ6m0U6Cw9ks68ysSn+XdB4tT9LEomxxaW/KjARH2BgSlLOUV/O4/jauzjtqZdCI4t7tXYWRzHY3r9FioqqNkMUn31V7DhMYllFvLKJwPZmjX4sZ+an+jw==\"",
    "remember-me": "true",
    "storage_test": "storage_test",
    "whatsapp-mutex": "\"x890275486:init_1508762385445\""
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