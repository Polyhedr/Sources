<a name="sources"></a>
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/sources_dark_theme.png" height="100px" />
    <img src="assets/sources_light_theme.png" height="100px" />
  </picture>
  <br />
  c a r d s &nbsp; & &nbsp; g a m e s
</p>

<p align="center">
  <a href="https://github.com/Polyhedr/Sources/tree/english?tab=readme-ov-file#sources"><img src="rule_lib/english_crop.png" alt="English" width="50px" height="30px"></a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/Polyhedr/Sources/tree/fran%C3%A7ais?tab=readme-ov-file#sources"><img src="rule_lib/french_crop.png" alt="French" width="50px" height="30px"></a>
</p>

<h6 align="center">
Sources is an innovative card game where every playthrough is unique: just pick a Rule card to discover a new way to play. And that’s not all: the game is designed to evolve with its community. You can modify existing rules or create new ones. We explain it all here...
</h6>

## Sources Cards 🃏🎴
**Sources** contains 78 cards, divided into **13 values** (from 0 to 12) and **6 colors** (yellow, orange, red, purple, blue, and green). Aesthetically, each color is linked to a distinct motif: for example, red is symbolized by fire, blue by water, etc.

<p align="center">
<img src="assets/some_cards.jpg">
</p>

The 6 colors are organized according to:
- **Three symbols**:  
  - **Square**: yellow and purple.  
  - **Circle**: orange and blue.  
  - **Triangle**: red and green.  
- **Two themes**:  
  - **Light**: yellow, red, and blue.  
  - **Dark**: orange, purple, and green.  

This system, inspired by traditional playing cards (red/black with ♥️♠️♦️♣️), ensures complete compatibility with classic games while opening the door to more complex rules.

<p align="center">
<img src="assets/color_ring.png" height="150px" />
</p>
  
The card colors are organized on a **color wheel**, where each color is connected to two natural neighbors. For example, **orange** is adjacent to **red** and **yellow**. This organization can be used in rules to create mechanics based on color proximity. The color wheel is designed to respect the alternation of themes (light/dark) and symbols (square, circle, triangle), with two opposite colors sharing the same symbol.

## Sources Games 🎮
Explore the complete collection of Sources games here.

|Game README|Rule Card|Duration|Age|Players|Cards|
|-----------|:-------:|--------|---|-------|-----|
|**[Two Towers](https://github.com/Polyhedr/Sources/tree/english/rules/Two_Towers#two-towers)**|[<img src="https://github.com/Polyhedr/Sources/blob/english/rules/Two_Towers/Two_Towers/rule_top.png" height=20px/>](https://github.com/Polyhedr/Sources/tree/english/rules/Two_Towers/Two_Towers/rule.pdf)|20 min|10+|2-6|0-10 🟡🟠🔴🟣🔵🟢|
| **[Skyzone](https://github.com/Polyhedr/Sources/tree/english/rules/Skyzone#skyzone)**|[<img src="https://github.com/Polyhedr/Sources/blob/english/rules/Skyzone/Skyzone/rule_top.png" height=20px/>](https://github.com/Polyhedr/Sources/tree/english/rules/Skyzone/Skyzone/rule.pdf)|20 min|12+|2-3|0-10 🟡🟠🔴🟣|
| **[Skyzone shape](https://github.com/Polyhedr/Sources/tree/english/rules/Skyzone#skyzone-shape)**|[<img src="https://github.com/Polyhedr/Sources/blob/english/rules/Skyzone/Skyzone_shape/rule_top.png" height=20px/>](https://github.com/Polyhedr/Sources/tree/english/rules/Skyzone/Skyzone_shape/rule.pdf)|20 min|12+|2-4|0-10 🟡🟠🔴🟣🔵🟢|
| **[Sup](https://github.com/Polyhedr/Sources/tree/english/rules/Sup#sup)**|[<img src="https://github.com/Polyhedr/Sources/blob/english/rules/Sup/Sup/rule_top.png" height=20px/>](https://github.com/Polyhedr/Sources/tree/english/rules/Sup/Sup/rule.pdf)|25 min|12+|2-6|1-12 🟡🟠🔴🟣🔵|
| **[Sup team](https://github.com/Polyhedr/Sources/tree/english/rules/Sup#sup-team)**|[<img src="https://github.com/Polyhedr/Sources/blob/english/rules/Sup/Sup_team/rule_top.png" height=20px/>](https://github.com/Polyhedr/Sources/tree/english/rules/Sup/Sup_team/rule.pdf)|25 min|12+|2-6|1-12 🟡🟠🔴🟣🔵|
| **[Unomytho](https://github.com/Polyhedr/Sources/tree/english/rules/Unomytho#unomytho)**|[<img src="https://github.com/Polyhedr/Sources/blob/english/rules/Unomytho/Unomytho/rule_top.png" height=20px/>](https://github.com/Polyhedr/Sources/tree/english/rules/Unomytho/Unomytho/rule.pdf)|20 min|6+|2-6|0-11 🟡🟠🔴🟣🔵🟢|
| **[Unomytho 1pile](https://github.com/Polyhedr/Sources/tree/english/rules/Unomytho#unomytho-1pile)**|[<img src="https://github.com/Polyhedr/Sources/blob/english/rules/Unomytho/Unomytho_1pile/rule_top.png" height=20px/>](https://github.com/Polyhedr/Sources/tree/english/rules/Unomytho/Unomytho_1pile/rule.pdf)|20 min|6+|2-6|0-11 🟡🟠🔴🟣🔵🟢|

## How Do Rule Cards Work? 📄
Each rule in **Sources** is associated with a **Rule Card**, generated from the **rule.tex** file (converted to PDF via lualatex). The card is double-sided and includes the following elements:

- **QR Code**: A QR code (**qr-code.png**) that links to the **README.md** file associated with the rule. This file provides additional details to clarify the rules if needed.
- **Game Logo**: The game logo (**logo_alpha.png**).
- **Game Information**: Includes age limit, card values and colors required, number of players, and average game duration.
- **Rule Summary**: A condensed version of the rules, often sufficient to start playing.

## Dependencies
**Windows (with [Chocolatey](https://community.chocolatey.org/)):**
```sh
choco install texlive imagemagick ghostscript
```
**Linux (with apt):**
```sh
sudo apt-get install texlive imagemagick ghostscript
```

## Create a New Rule ✨
Want to add a new rule to **Sources**? Follow these steps to contribute:
1. **Create the rule file**: Write a **rule.tex** file describing your new rule.
2. **Add a QR Code**: Generate a QR code (**qr-code.png**) using [QRCode Monkey](https://www.qrcode-monkey.com/). This QR code should link to a **README.md** file containing:
   - A detailed explanation of the rule.
   - Examples or gameplay tips if needed.
3. **Add a Logo**: Include a **logo_alpha.png** file to visually represent your rule (1800x624 px).
4. **Generate the PDF Card**: Use **lualatex** to transform the **rule.tex** file into a double-sided PDF card.
5. **Submit Your Rule**: Propose your rule to the community by creating a pull request in the **Sources** repository.

For any questions, feel free to open an issue to discuss with the community. 🚀

## Modify an Existing Rule ✏️
If you want to modify an existing rule, here are two options:
1. **Open an Issue**: If you identify a problem or an improvement, open an issue to discuss it with the community. 🗣️
2. **Submit a Pull Request**: Directly edit the **rule.tex** file and the associated **README.md**, then submit a pull request to propose your changes. 🔧

## Other Compatible Games ♻️
Know of or looking for an existing game compatible with **Sources**? This section is for you! 🔍  
We list games compatible with **Sources** here. If you know of a compatible game not yet listed, feel free to open an issue or submit a pull request! 💡

|Game|Details|
|-------------|-----------|
|[Mastermind](https://en.wikipedia.org/wiki/Mastermind_(board_game))|The coder selects 4 cards from the first 24 cards (0-3 of the 6 colors) and keeps the remaining 20 face down. These cards are used as clues: "Correct but misplaced": card placed horizontally, face down; "Correct and well placed": card placed vertically, face down. The limited number of cards, compared to the classic Mastermind, does not pose a challenge for a logical player who ensures consistency between their attempts.|

