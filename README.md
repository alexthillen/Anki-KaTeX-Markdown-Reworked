# Anki Markdown

[Download Anki Add-On](https://ankiweb.net/shared/info/1786114227)

Adding support and improvements of how cards are displayed.
Allowing for clozes inside code blocks. Better night mode support & readability. Coloring of the cloze elements. 

Creates a new Basic and a new Cloze Note Type that support Markdown and KaTeX: *Markdown and KaTeX Basic (Color)* and *Markdown and KaTeX Cloze (Color)*.

The following can be used to create a sample cloze card (remove the "\\" before the backticks).

```md
# A Dummy Card
## Subtitle
### Math
- {{c1::$\pi=3.1415...$::$\pi=...$}}
### Escaping dollar
$$1\$ < 1€ $$ after

### Escaped c++ code :

\```cpp
#include <stdio.h>
{{c2::boost\:\:add_vertex::how to add vertex in boost}}(...);
\```

### Python

\```py
def print_hello():
  print("{{c2::hello}}")
\```
```

![Front Code](.github/assets/image.png)
![Back Code](.github/assets/image-1.png)
![Math Front](.github/assets/image-2.png)
![Math Back](.github/assets/image-3.png)
![Light Mode](.github/assets/image-4.png)


## Features

- <a href="https://www.intmath.com/cg5/katex-mathjax-comparison.php" rel="nofollow">KaTeX is considered way faster than MathJax</a>
- Works on any device as long as there is internet connection
- <a href="https://markdown-it.github.io/" rel="nofollow">Markdown is a great all in one solution for Anki cards</a>
- Access KaTeX by <code>$...$</code> for inline math or <code>$$...$$</code> for displaystyle math, a list of supported functions can be found <a href="https://katex.org/docs/supported.html" rel="nofollow">here</a> 
- MathJax can also be accessed via <code>\[ ... \]</code> and <code>\(...\)</code>
- Escape `\$` and `\:`
- colored cloze cards
- support for dark mode


## Customizing Styles
It's possible to customize the note style by editing **"_user_style.css"** inside the media folder. To find out where your media folder is, please refer to the [Anki documentation](https://docs.ankiweb.net/files.html#file-locations).

If a value has already been set inside the default **"_style.css"**, you can overwrite it by using the `!important` flag.
If you want to remove a value, you can also use the `unset` keyword.

```css
/* _user_style.css example */

.nightMode, .night-mode, .night_mode {
  background-color: #1e1e2e !important; /* overwrite value */
}
.nightMode code {
  filter: unset !important; /* remove value */
}

/* !important is not necessary here since ".field" is not set in "_style.css" */
.field {
  display: inline-block;
  text-align: left;
}

```

The markdown preview will automatically follow all user style modifications.

## Used Libraries
<a href="https://github.com/markdown-it/markdown-it">Markdown-It</a>  
<a href="https://github.com/KaTeX/KaTeX">KaTeX</a>

## Installation
* Go to
<a href="https://ankiweb.net/shared/info/1786114227"><img src="https://preview.redd.it/fka0b5cc48t41.png?auto=webp&s=c26da98dca2863e1d0dddbfd59b5bea6165f4bcb" width="24"></a>
to see how to install this addon for anki
* To install locally download the latest [release](https://github.com/alexthillen/Anki-KaTeX-Markdown-Reworked/releases) and install by opening **Anki → Tools → Add-ons → Install** from file, then select **MDKaTeX.ankiaddon**

Fork of : https://github.com/Jwrede/Anki-KaTeX-Markdown.

## Credits to
- [Jwrede](https://github.com/Jwrede) for starting this cool project.
- [Eljamm](https://github.com/eljamm) for his substantial contributions with dynamic styling and significantly enhancing the code's maintainability.
