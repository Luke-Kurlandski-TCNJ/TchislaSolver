options(stringsAsFactors=FALSE)

library(dplyr)
library(lubridate)
library(ggplot2)
library(shiny)
library(gridExtra)
library(reticulate)
library(stringr)

theme_set(theme_bw())

ui <- fluidPage(

    titlePanel("Tchisla Solver"),

    sidebarLayout(
        sidebarPanel(
            numericInput(inputId="use", label="Enter one Number to Use", value=4),
            textInput(inputId="targets", label="Enter comma-separated list of Targets", value="3, 4, 5"),
            numericInput(inputId="maxPow", label="Enter the maximum power bound", value=20000),
            numericInput(inputId="maxFact", label="Enter the maximum factorial bound", value=140*140),
            numericInput(inputId="maxRec", label="Enter the maximum recursion depth", value=10000),
            numericInput(inputId="tooBig", label="Enter the maximum storage bound exponenent (below: 10^24)", value=24)
        ),
    

        mainPanel(
            uiOutput("calculate")
        )
    )
)

server <- function(input, output) {

    output$calculate <- renderUI({
        source_python("tchisla.py")
        numTargets <- str_length(str_replace_all(input$targets, "[, ]", ""))
        x <- calculate(input$use, input$targets)
        strs <- paste(x[[1]][[1]], " = ", x[[1]][[2]], " with ", x[[1]][[3]], " uses.\n")
        for (i in 2:numTargets) {
            strs <- paste(strs, paste(x[[i]][[1]], " = ", x[[i]][[2]], " with ", x[[i]][[3]], " uses.\n"), sep = '<br/>')
        }
        HTML(strs)
    })
    
    
}

# Run the application 
shinyApp(ui = ui, server = server)
