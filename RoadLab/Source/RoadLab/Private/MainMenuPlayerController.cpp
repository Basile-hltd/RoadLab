// Fill out your copyright notice in the Description page of Project Settings.


#include "MainMenuPlayerController.h"
#include "Blueprint/UserWidget.h"

AMainMenuPlayerController::AMainMenuPlayerController()
{
    UE_LOG(LogTemp, Display, TEXT("MainMenuPlayerController CONSTRUCTED"));

}

void AMainMenuPlayerController::BeginPlay() {
    
    Super::BeginPlay();
    
    SetShowMouseCursor(true);


    if (MainMenuWidgetClass)
    {
        MainMenuWidget = CreateWidget<UUserWidget>(this, MainMenuWidgetClass);

        if (MainMenuWidget)
        {
            MainMenuWidget->AddToViewport();
            UE_LOG(LogTemp, Warning, TEXT("UI added to viewport"));
        }
        else {
            UE_LOG(LogTemp, Warning, TEXT("MainMenuWidget not CONSTRUCTED"));
        }
    }
    else {
        UE_LOG(LogTemp, Warning, TEXT("MainMenuWidgetClass not CONSTRUCTED"));
    }
}
