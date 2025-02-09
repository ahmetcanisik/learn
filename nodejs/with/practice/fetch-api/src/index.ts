async function getApi(apiServer: string) {
  try {
    const res = await fetch(apiServer);
    if (res.status === 200) {
      const data = await res.json();
      return data;
    }
  } catch (e: any) {
    console.error(
      `When sending request on the ${apiServer} catching errors -> `,
      e
    );
  }
}


async function main() {
    const myHTMLSkill = await getApi("https://api.ahmetcanisik.com/skills");

    myHTMLSkill.forEach((skill: any, index: number) => {
        let progressBar = "";

        for (let i = 0; i < (skill.progress / 10); i++) {
            progressBar += "*";
        };

        console.log(`${progressBar}\t\t -> ${skill.name}`);
    });
}

(async() => await main())();