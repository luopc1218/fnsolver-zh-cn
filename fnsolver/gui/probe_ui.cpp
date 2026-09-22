#include "probe_ui.h"
#include <QCoreApplication>
#include <unordered_map>

QString probe_display_name(const Probe* probe) {
  // This needs to be inside the function definition to ensure translation is initialized before trying to get text.
  static const std::unordered_map<std::string, QString> probe_display_names{
    {"X", QCoreApplication::translate("probe_ui", "Locked")},
    {"-", QCoreApplication::translate("probe_ui", "Basic")},
    {"M1", QCoreApplication::translate("probe_ui", "Mining G1")},
    {"M2", QCoreApplication::translate("probe_ui", "Mining G2")},
    {"M3", QCoreApplication::translate("probe_ui", "Mining G3")},
    {"M4", QCoreApplication::translate("probe_ui", "Mining G4")},
    {"M5", QCoreApplication::translate("probe_ui", "Mining G5")},
    {"M6", QCoreApplication::translate("probe_ui", "Mining G6")},
    {"M7", QCoreApplication::translate("probe_ui", "Mining G7")},
    {"M8", QCoreApplication::translate("probe_ui", "Mining G8")},
    {"M9", QCoreApplication::translate("probe_ui", "Mining G9")},
    {"M10", QCoreApplication::translate("probe_ui", "Mining G10")},
    {"R1", QCoreApplication::translate("probe_ui", "Research G1")},
    {"R2", QCoreApplication::translate("probe_ui", "Research G2")},
    {"R3", QCoreApplication::translate("probe_ui", "Research G3")},
    {"R4", QCoreApplication::translate("probe_ui", "Research G4")},
    {"R5", QCoreApplication::translate("probe_ui", "Research G5")},
    {"R6", QCoreApplication::translate("probe_ui", "Research G6")},
    {"B1", QCoreApplication::translate("probe_ui", "Booster G1")},
    {"B2", QCoreApplication::translate("probe_ui", "Booster G2")},
    {"D", QCoreApplication::translate("probe_ui", "Duplicator")},
    {"S", QCoreApplication::translate("probe_ui", "Storage")},
    {"C", QCoreApplication::translate("probe_ui", "Combat")}
  };
  return probe_display_names.at(probe->shorthand);
}
