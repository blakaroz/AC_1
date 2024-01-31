const os = require("os");
const local = {
    "home directory": os.homedir(),
    "oper sys": os.type(),
    "lsast rebook": os.uptime(),
    "network": os.networkInterfaces()


}
console.log(local)