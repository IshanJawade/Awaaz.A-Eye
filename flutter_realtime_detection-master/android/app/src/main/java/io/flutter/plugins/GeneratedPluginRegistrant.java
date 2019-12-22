package io.flutter.plugins;

import io.flutter.plugin.common.PluginRegistry;
import io.flutter.plugins.camera.CameraPlugin;
import fr.g123k.deviceapps.DeviceAppsPlugin;
import com.flutter.text_to_speech.FlutterTextToSpeechPlugin;
import com.tundralabs.fluttertts.FlutterTtsPlugin;
import sq.flutter.tflite.TflitePlugin;

/**
 * Generated file. Do not edit.
 */
public final class GeneratedPluginRegistrant {
  public static void registerWith(PluginRegistry registry) {
    if (alreadyRegisteredWith(registry)) {
      return;
    }
    CameraPlugin.registerWith(registry.registrarFor("io.flutter.plugins.camera.CameraPlugin"));
    DeviceAppsPlugin.registerWith(registry.registrarFor("fr.g123k.deviceapps.DeviceAppsPlugin"));
    FlutterTextToSpeechPlugin.registerWith(registry.registrarFor("com.flutter.text_to_speech.FlutterTextToSpeechPlugin"));
    FlutterTtsPlugin.registerWith(registry.registrarFor("com.tundralabs.fluttertts.FlutterTtsPlugin"));
    TflitePlugin.registerWith(registry.registrarFor("sq.flutter.tflite.TflitePlugin"));
  }

  private static boolean alreadyRegisteredWith(PluginRegistry registry) {
    final String key = GeneratedPluginRegistrant.class.getCanonicalName();
    if (registry.hasPlugin(key)) {
      return true;
    }
    registry.registrarFor(key);
    return false;
  }
}
