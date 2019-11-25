{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "kernelspec": {
      "display_name": "R",
      "language": "R",
      "name": "ir"
    },
    "language_info": {
      "codemirror_mode": "r",
      "file_extension": ".r",
      "mimetype": "text/x-r-source",
      "name": "R",
      "pygments_lexer": "r",
      "version": "3.3.1"
    },
    "colab": {
      "name": "R.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/cristianmejia00/practice/blob/master/R.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "B1twa2IpVdz8",
        "colab_type": "text"
      },
      "source": [
        "Code without visible output:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6wS7JsFGVd0C",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "a <- 8"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5a-Tl6NrVd0M",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "b <- 4:10"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5LMMs9s5Vd0R",
        "colab_type": "text"
      },
      "source": [
        "With visible output:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "y4kK69H8Vd0T",
        "colab_type": "code",
        "outputId": "76e70c47-d19d-4eca-df8d-239bcf23cad3",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 164
        }
      },
      "source": [
        "a + b"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "[1] 12 13 14 15 16 17 18"
            ],
            "text/latex": "\\begin{enumerate*}\n\\item 12\n\\item 13\n\\item 14\n\\item 15\n\\item 16\n\\item 17\n\\item 18\n\\end{enumerate*}\n",
            "text/markdown": "1. 12\n2. 13\n3. 14\n4. 15\n5. 16\n6. 17\n7. 18\n\n\n",
            "text/html": [
              "<ol class=list-inline>\n",
              "\t<li>12</li>\n",
              "\t<li>13</li>\n",
              "\t<li>14</li>\n",
              "\t<li>15</li>\n",
              "\t<li>16</li>\n",
              "\t<li>17</li>\n",
              "\t<li>18</li>\n",
              "</ol>\n"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "HfrCTyHxVd0b",
        "colab_type": "text"
      },
      "source": [
        "Printing is captured and sent to the frontend:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "3RuTihGeVd0d",
        "colab_type": "code",
        "outputId": "4bff770b-98e8-4d9c-a776-e53b50e49604",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "print('Hello world! Love, R in Jupyter.')"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[1] \"Hello world! Love, R in Jupyter.\"\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "PBBG3dNuVd0i",
        "colab_type": "text"
      },
      "source": [
        "So are errors:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Yl0YmWZfVd0k",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "f2 <- function() stop('deep error')\n",
        "throw <- function() f2()"
      ],
      "execution_count": 0,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5BBfn7Q8Vd0p",
        "colab_type": "code",
        "outputId": "a4186c96-7c0a-4992-b3ed-08a384192a2f",
        "colab": {}
      },
      "source": [
        "'this line is run / displayed'\n",
        "throw()\n",
        "'this line is not run / displayed'"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "'this line is run / displayed'"
            ],
            "text/latex": "'this line is run / displayed'",
            "text/markdown": "'this line is run / displayed'",
            "text/plain": [
              "[1] \"this line is run / displayed\""
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "error",
          "ename": "ERROR",
          "evalue": "Error in f2(): deep error\n",
          "traceback": [
            "Error in f2(): deep error\nTraceback:\n",
            "1. throw()",
            "2. f2()   # at line 2 of file <text>",
            "3. stop(\"deep error\")   # at line 1 of file <text>"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "lS7Zet53Vd0u",
        "colab_type": "text"
      },
      "source": [
        "Plotting works too:"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SPjRljbTVd0v",
        "colab_type": "code",
        "outputId": "376c9734-0526-4c6f-df5a-72ef7016dbf3",
        "colab": {}
      },
      "source": [
        "x <- seq(0, 2*pi, length.out=50)\n",
        "plot(x, sin(x))"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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",
            "text/plain": [
              "plot without title"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    }
  ]
}