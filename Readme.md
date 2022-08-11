<h1 align="center"> Conversion from the decimal system to other systems </h1>

<h2> Summary </h2> 
___________________
<p> This project </p>
<p align="center">
    <a href= "#About">About </a> *
    <a href= "#Requirements">Requirements </a> *
    <a href= "#Problem">Problem </a> *
    <a href= "#Solution">Solution </a> *
    <a href= "#Method">Method </a> *
</p>

# About
<p> Create an algorithm to convert decimal numbers to any other base </p>

# Requirements
<p> I recommend running in some IDE such as Jupyter Notebook, VS Code </p>

# Problem
<p> I need to convert from decimal system to other systems. However, it is a laborious process to perform manually. </p>

# Solution
<p> Create an algorithm that converts decimal to any other base </p>

# Method
<p> 

To convert an integer from the decimal system to another system, the number is successively divided by the base of the desired system, noting the remainders of the divisions, until it is no longer possible to perform the division, that is, when the quotient is equal to zero. The sequence composed of the remainders of the successive divisions, in the reverse order in which they were obtained, corresponds to the number in the new numbering system. 

To convert to the hexadecimal system (base 16), we need 16 digits. In order not to create new figures, the letters A to F are used, taking advantage of the alphabetical order. The following table presents the values corresponding, in the decimal system, to the letters used as figures in the hexadecimal system: 

<table>
    <tr>
        <td>hexadecimal system</td>
        <td>decimal system</td>
    </tr>
    <tr>
        <td>A</td>
        <td>10</td>
    </tr>
    <tr>
        <td>B</td>
        <td>11</td>
    </tr>
    <tr>
        <td>C</td>
        <td>12</td>
    </tr>
     <tr>
        <td>D</td>
        <td>13</td>
    </tr>
    <tr>
        <td>E</td>
        <td>14</td>
    </tr>
    <tr>
        <td>F</td>
        <td>15</td>
    </tr>
</p>

