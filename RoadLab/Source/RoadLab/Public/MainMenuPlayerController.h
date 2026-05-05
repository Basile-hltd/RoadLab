// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/PlayerController.h"
#include "MainMenuPlayerController.generated.h"

/**
 * 
 */
UCLASS()
class ROADLAB_API AMainMenuPlayerController : public APlayerController
{
	GENERATED_BODY()
	
public:
	AMainMenuPlayerController();
	
	void BeginPlay();

	UPROPERTY(EditDefaultsOnly)
	TSubclassOf<class UUserWidget> MainMenuWidgetClass;

	UUserWidget* MainMenuWidget = nullptr;

};
