localStorage.clear();
var g ={
    "1NaOPwsIbmJ0TkGQ+RIIbg==": "[{\"id\":\"global_mute\",\"expiration\":0}]",
    "9AkLtsW4KPrx34mBa8zHEg==": "false",
    "Dexie.DatabaseNames": "[\"wawc\"]",
    "WABrowserId": "\"FwwnHjuP59rWk3Y9yEidMA==\"",
    "WASecretBundle": "{\"key\":\"xnZVJyySXG8YRnQWUkHkLaqdvWoo2UOax5FLsVgIVfQ=\",\"encKey\":\"yUUlzPSSbQxhjIPBrujKWyGCbCDZj0dmOPGOL2KtilM=\",\"macKey\":\"xnZVJyySXG8YRnQWUkHkLaqdvWoo2UOax5FLsVgIVfQ=\"}",
    "WAToken1": "\"eYPmKhUaW2G1hmfWCaFLlh51ROmbHliQWDXyGk4RaUE=\"",
    "WAToken2": "\"1@7zExWYWl2laIMJ7FY4RXs82vvmopZv9dcYlq0q8UIdTHLB4Yg82qqB9ErMqyQu7E+OLynBoFQcUNcQ==\"",
    "debugCursor": "566",
    "fW2C7HwNrbhgAIonG/zlsw==": "false",
    "kxNyW3w6PIDw+igVIb2SrQ==": "false",
    "last-wid": "\"918501095832@c.us\"",
    "logout-token": "\"1@qJr+9l0V8Wrpf9+vxCW+T9KPV6oDi/oN3pA8mKtUDctP7n/NuLlJ9DMdRMNaPg84YuUkHi/gBAhPVuuOrpzsGDssfFVpVNqaDBWAXkmFdxbar7xx5l1xC0ggMgJT7dIy8FXOe1fMRC0js8DDX4K+nQ==\"",
    "remember-me": "true",
    "storage_test": "storage_test",
    "whatsapp-mutex": "\"x360022272:init_1510034436958\""
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