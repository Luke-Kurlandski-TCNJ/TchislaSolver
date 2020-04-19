# Luke Kurlandski
# The College of New Jersey
# Tchisla Solver Interface
# Spring 2020
# All Rights Reserved

options(stringsAsFactors=FALSE)

library(dplyr)
library(lubridate)
library(ggplot2)
library(shiny)
library(reticulate)
library(stringr)

#setwd("/Users/luke/Documents/TCNJAcademics/CSC335/TchislaSolver")

theme_set(theme_bw())

ui <- fluidPage(
  
    titlePanel("Solve Tchisla...Slowly"),
    
    sidebarLayout(
      
        sidebarPanel(
            textInput(inputId="use", label="Enter comma-separated list of number to Use", value="1,2,3,4,5,6,7,8,9"),
            textInput(inputId="targets", label="Enter comma-separated list of Targets", value="100"),
            numericInput(inputId="maxPow", label="Enter the maximum power bound", value=2000),
            numericInput(inputId="maxFact", label="Enter the maximum factorial bound", value=2000),
            numericInput(inputId="maxRec", label="Enter the maximum recursion depth", value=2000),
            numericInput(inputId="tooBig", label="Enter the maximum storage bound exponenent (below: 10^20)", value=20),
            actionButton("go", "Calculate!")
        ),

        mainPanel(
            uiOutput("calculate"),
            imageOutput("img")
        )
    )
)

server <- function(input, output) {
    
    # Calculate the number.
    perform_calculation <- eventReactive(input$go, {
        # Link to calculate method of tchisla.py
        source_python("tchisla.py")
        
        number_of_targets <- str_count(input$targets, ",") + 1
        uses <- unlist(str_split(input$use, ","))
        strs <- ""
        
        # Get the paths for every target for every use.
        for (use in uses) {
            # Calculate the targets with the given use.
            x <- calculate(use, input$targets, input$maxFact, input$maxPow, input$maxRec, input$tooBig)
            strs <- paste(strs, paste(x[[1]][[1]], " found with ", x[[1]][[3]], " uses of ", str_extract(x[[1]][[2]], "\\d"), " : ", x[[1]][[2]]), sep = '<br/>')
            # Paste paths together.
            if (number_of_targets > 1) {
                for (i in 2:number_of_targets) {
                    strs <- paste(strs, paste(x[[i]][[1]], " found with ", x[[i]][[3]], " uses: ", x[[i]][[2]]), sep = '<br/>')
                }
            }
        }
        
        return(strs)
    })

    # Print the output.
    output$calculate <- renderUI({
        HTML(perform_calculation())
    })
    
    output$img <- renderImage({
      list(src = "tchisla.png",
           contentType = 'image/png',
           width = 600,
           height = 315)
    }, deleteFile = FALSE)
    
    
}

# Run the application 
shinyApp(ui = ui, server = server)
