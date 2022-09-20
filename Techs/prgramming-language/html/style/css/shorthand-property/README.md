2014年8月28日21:26:49
学习CSS的教程的时候发现好多个shorthand property的属性，为了担心之后混淆，所以把它们总结一下：

## Background - Shorthand property

The shorthand property for background is simply "background":
body {
    background: #ffffff url("img_tree.png") no-repeat right top;
}

 When using the shorthand property the order of the property values is:
background-color
background-image
background-repeat
background-attachment
background-position
It does not matter if one of the property values is missing, as long as the ones that are present are in this order.

## List - Shorthand property

The shorthand property used for lists, is the list-style property:
ul {
    list-style: square url("sqpurple.gif");
}

When using the shorthand property, the order of the values are:
list-style-type
list-style-position (for a description, see the CSS properties table below)
list-style-image
It does not matter if one of the values above are missing, as long as the rest are in the specified order.

## Border - Shorthand property

p {
    border: 5px solid red;
}

The border property is a shorthand for the following individual border properties:
border-width
border-style (required)
border-color

## Margin - Shorthand property

The shorthand property for all the margin properties is "margin":
p {
    margin: 100px 50px;
}

The margin property can have from one to four values.
margin: 25px 50px 75px 100px;
top margin is 25px
right margin is 50px
bottom margin is 75px
left margin is 100px

margin: 25px 50px 75px;
top margin is 25px
right and left margins are 50px
bottom margin is 75px

margin: 25px 50px;
top and bottom margins are 25px
right and left margins are 50px

margin: 25px;
all four margins are 25px

## Padding - Shorthand property

The shorthand property for all the padding properties is "padding":
p {
    padding: 25px 50px;
}

The padding property can have from one to four values.
padding: 25px 50px 75px 100px;
top padding is 25px
right padding is 50px
bottom padding is 75px
left padding is 100px

padding: 25px 50px 75px;
top padding is 25px
right and left paddings are 50px
bottom padding is 75px

padding: 25px 50px;
top and bottom paddings are 25px
right and left paddings are 50px

padding: 25px;
all four paddings are 25px



