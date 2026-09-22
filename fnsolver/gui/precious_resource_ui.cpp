#include "precious_resource_ui.h"
#include <unordered_map>
#include <QCoreApplication>

QString precious_resource_display_name(precious_resource::Type precious_resource) {
  // This needs to be inside the function definition to ensure translation is initialized before trying to get text.
  static const std::unordered_map<precious_resource::Type, QString> precious_resource_display_names{
    {precious_resource::Type::arc_sand_ore, QCoreApplication::translate("precious_resource_ui", "Arc Sand Ore")},
    {precious_resource::Type::aurorite, QCoreApplication::translate("precious_resource_ui", "Aurorite")},
    {precious_resource::Type::white_cometite, QCoreApplication::translate("precious_resource_ui", "White Cometite")},
    {precious_resource::Type::enduron_lead, QCoreApplication::translate("precious_resource_ui", "Enduron Lead")},
    {precious_resource::Type::everfreeze_ore, QCoreApplication::translate("precious_resource_ui", "Everfreeze Ore")},
    {precious_resource::Type::foucaultium, QCoreApplication::translate("precious_resource_ui", "Foucaultium")},
    {precious_resource::Type::lionbone_bort, QCoreApplication::translate("precious_resource_ui", "Lionbone Bort")},
    {precious_resource::Type::infernium, QCoreApplication::translate("precious_resource_ui", "Infernium")},
    {precious_resource::Type::boiled_egg_ore, QCoreApplication::translate("precious_resource_ui", "Boiled-Egg Ore")},
    {precious_resource::Type::marine_rutile, QCoreApplication::translate("precious_resource_ui", "Marine Rutile")},
    {precious_resource::Type::dawnstone, QCoreApplication::translate("precious_resource_ui", "Dawnstone")},
    {precious_resource::Type::cimmerian_cinnabar, QCoreApplication::translate("precious_resource_ui", "Cimmerian Cinnabar")},
    {precious_resource::Type::ouroboros_crystal, QCoreApplication::translate("precious_resource_ui", "Ouroboros Crystal")},
    {precious_resource::Type::parhelion_platinum, QCoreApplication::translate("precious_resource_ui", "Parhelion Platinum")},
    {precious_resource::Type::bonjelium, QCoreApplication::translate("precious_resource_ui", "Bonjelium")}
  };
  return precious_resource_display_names.at(precious_resource);
}
