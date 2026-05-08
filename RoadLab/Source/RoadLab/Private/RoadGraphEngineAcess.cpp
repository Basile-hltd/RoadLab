// Fill out your copyright notice in the Description page of Project Settings.


#include "RoadGraphEngineAcess.h"

URoadGraphEngineAcess::URoadGraphEngineAcess(){
	UE_LOG(LogTemp, Log, TEXT("RoadGraphEngine : Constructor"));
}

URoadGraphEngineAcess::~URoadGraphEngineAcess(){
}

void URoadGraphEngineAcess::StartProcess(float lat, float lon, float diam) {
	UE_LOG(LogTemp, Log, TEXT("RoadGraphEngine : start external process"));
}
