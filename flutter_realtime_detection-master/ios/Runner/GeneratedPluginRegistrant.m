//
//  Generated file. Do not edit.
//

#import "GeneratedPluginRegistrant.h"
#import <camera/CameraPlugin.h>
#import <device_apps/DeviceAppsPlugin.h>
#import <flutter_text_to_speech/FlutterTextToSpeechPlugin.h>
#import <flutter_tts/FlutterTtsPlugin.h>
#import <tflite/TflitePlugin.h>

@implementation GeneratedPluginRegistrant

+ (void)registerWithRegistry:(NSObject<FlutterPluginRegistry>*)registry {
  [CameraPlugin registerWithRegistrar:[registry registrarForPlugin:@"CameraPlugin"]];
  [DeviceAppsPlugin registerWithRegistrar:[registry registrarForPlugin:@"DeviceAppsPlugin"]];
  [FlutterTextToSpeechPlugin registerWithRegistrar:[registry registrarForPlugin:@"FlutterTextToSpeechPlugin"]];
  [FlutterTtsPlugin registerWithRegistrar:[registry registrarForPlugin:@"FlutterTtsPlugin"]];
  [TflitePlugin registerWithRegistrar:[registry registrarForPlugin:@"TflitePlugin"]];
}

@end
