// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "UObject/Object.h"
#include "GenericPlatform/GenericPlatformProcess.h"
#include "RoadGraphEngineAcess.generated.h"

/**
 * 
 */
UCLASS(BlueprintType)
class ROADLAB_API URoadGraphEngineAcess : public UObject {
	
	GENERATED_BODY()

public:
	URoadGraphEngineAcess();
	~URoadGraphEngineAcess();

	UFUNCTION(BlueprintCallable)
	void StartProcess(float lat, float lon, float diam);

};
