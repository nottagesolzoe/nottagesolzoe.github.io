import {cp,writeFile} from "node:fs/promises";
await cp(new URL("./out/",import.meta.url),new URL("../",import.meta.url),{recursive:true});
await writeFile(new URL("../.nojekyll",import.meta.url), "");
console.log("Static portfolio copied to the GitHub Pages root.");
