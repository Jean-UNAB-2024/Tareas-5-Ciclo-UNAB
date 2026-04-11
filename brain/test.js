import fs from 'node:fs'

const FolderBaseName = '_Semana'

try{
    for (let i = 1; i <= 16; i++) {
        let newFolderName = `./Electrónica/${i}${FolderBaseName}`
        if (!fs.existsSync(newFolderName)) {
            fs.mkdirSync(newFolderName);
        }
    }
    // fs.mkdirSync('Administracion_y_Gestion_de_Base_de_Datos')
    // fs.mkdirSync('Catedra_UNAB')
    // fs.mkdirSync('Dinamica_de_Simulacion_de_Sistemas')
    // fs.mkdirSync('Electrónica')
}catch(e){
    console.error(`Error: ${e}`)
}