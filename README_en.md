# Mini Settlers Calculator

[中文版本](./README.md)

Welcome to the Mini Settlers Calculator! This tool is designed to assist with production calculations for the game [Mini Settlers](https://store.steampowered.com/app/2521630/_Mini_Settlers/). Simply input the **target products** and **quantities** to calculate the required **number of buildings** and **building relationships**. With this tool, you can avoid complex rate calculations and focus on planning buildings and logistics in the game.

![珍珠岛](.\figs\珍珠岛.png)

## Features

- Calculate for single or multiple target products
- Select production recipes
- Configure external inputs (for calculations across multiple islands)
- View the total number of buildings required
- View the complete building relationship tree
- View the sources and destinations of individual resources

## How to Use (The English version is currently being translated and will be available soon.)

1. **Generate or Update Building Recipe Table:**
   - Update recipes in the file `.\src\crafting_table_create_zh.py`.
   - Navigate to the `.\src\` directory and run `python crafting_table_create_zh.py` to generate the recipe file `buildings_zh.json`.
2. **Using the Calculator:**
   - Navigate to the `.\src\` directory and run `python ui.py`.
   - Input the target products and quantities, e.g., `Level 1 Population 240 Level 2 Population 1620 Level 3 Population 6600`.
   - Select production recipes for materials.
   - Configure external input materials.
   - View the results:
     - **Building Quantity**: Overview of the total number of buildings required (values rounded up).
     - **Building Relationship**: Complete building relationship tree.
     - **Resource Production Tree**: View the sources and destinations of individual resources (most commonly used feature).

## Reference Glossary

The English version is currently being translated and will be available soon.