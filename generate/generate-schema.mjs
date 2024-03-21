import { resolve } from "path";
import * as fs from "fs/promises";
import * as TJS from "typescript-json-schema";

// optionally pass argument to schema generator
const settings = {
  required: true,
};

// optionally pass ts compiler options
const compilerOptions = {
  strictNullChecks: true,
  esModuleInterop: true,
};

// optionally pass a base path
const basePath = "./my-dir";
const inputFilePath = "node_modules/antd/lib/index.d.ts";
const program = TJS.getProgramFromFiles(
  [resolve(inputFilePath)],
  compilerOptions,
  //   basePath
);

// Function to extract <Name>Props and save to a JSON file
async function extractPropsAndSaveToFile(inputFilePath, outputFilePath) {
  try {
    // Read the input file
    const data = await fs.readFile(inputFilePath, "utf8");

    // Regular expression to match <Name>Props
    const propsPattern = /(?<!as) (\w+Props) /g;

    // Extract matches
    let match;
    const propsList = [];
    while ((match = propsPattern.exec(data)) !== null) {
      if (match[1] == "ListProps") {
        // for some reason we crash on ListProps, lets skip it for now
        continue;
      }
      propsList.push(match[1]);
    }

    // Save to a JSON file
    await fs.writeFile(outputFilePath, JSON.stringify(propsList, null, 4));
    console.log("Props extracted and saved to:", outputFilePath);
    return propsList;
  } catch (err) {
    console.error("Error:", err);
  }
}
const outputFilePath = "./generate/propslist.json"; // Replace with your desired output file path

const propsList = await extractPropsAndSaveToFile(inputFilePath, outputFilePath);

// We can either get the schema for one file and one type...
// const schema = TJS.generateSchema(program, propsList, settings);
const generator = TJS.buildGenerator(program, settings);
// generator.getSchemaForSymbols(["ListProps"]);
// const schema = generator.getSchemaForSymbols(["ButtonProps", "DatePickerProps", "FlexProps"]);
propsList.forEach((props) => {
  // try {
  console.log(props);
  generator.getSchemaForSymbol(props);
  // } catch (err) {
  //     console.error('Error:', err);
  // }
});
const schema = generator.getSchemaForSymbols(propsList);

await fs.writeFile("./generate/schema.json", JSON.stringify(schema, undefined, 4), function (err) {
  if (err) {
    return console.log(err);
  }
  console.log("The file was saved!");
});

// // ... or a generator that lets us incrementally get more schemas

// const generator = TJS.buildGenerator(program, settings);

// // generator can be also reused to speed up generating the schema if usecase allows:
// const schemaWithReusedGenerator = TJS.generateSchema(program, "MyType", settings, [], generator);

// all symbols
// const symbols = generator.getUserSymbols();

// Get symbols for different types from generator.
// generator.getSchemaForSymbol("MyType");
// generator.getSchemaForSymbol("AnotherType");
