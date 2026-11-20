"""Prompt Mage Studio: independent prerelease entry point."""
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
WEB_DIRECTORY = "./web"
from .py.nodes.grimoire import PromptMageGrimoire
NODE_CLASS_MAPPINGS["PromptMageStudioGrimoire"] = PromptMageGrimoire
NODE_DISPLAY_NAME_MAPPINGS["PromptMageStudioGrimoire"] = "Prompt Mage Studio · Grimoire (Beta)"
from .py.nodes.grimoire import PromptMageGrimoireTurn
NODE_CLASS_MAPPINGS["PromptMageStudioGrimoireTurn"] = PromptMageGrimoireTurn
NODE_DISPLAY_NAME_MAPPINGS["PromptMageStudioGrimoireTurn"] = "Prompt Mage Studio · Grimoire Turn (Internal)"
from .py.nodes.spell_scroll import PromptMageSpellScroll
NODE_CLASS_MAPPINGS["PromptMageStudioSpellScroll"] = PromptMageSpellScroll
NODE_DISPLAY_NAME_MAPPINGS["PromptMageStudioSpellScroll"] = "Prompt Mage Studio · Spell Scroll"
from .py.nodes.foundry import PromptMageFoundry
NODE_CLASS_MAPPINGS["PromptMageStudioFoundry"] = PromptMageFoundry
NODE_DISPLAY_NAME_MAPPINGS["PromptMageStudioFoundry"] = "Prompt Mage Studio · Foundry (Experimental)"
from .py.nodes.foundry import PromptMageFoundryPlan
NODE_CLASS_MAPPINGS["PromptMageStudioFoundryPlan"] = PromptMageFoundryPlan
NODE_DISPLAY_NAME_MAPPINGS["PromptMageStudioFoundryPlan"] = "Prompt Mage Studio · Foundry Plan (Internal)"
from .py.nodes.foundry import PromptMageFoundryReviewSaved
NODE_CLASS_MAPPINGS["PromptMageStudioFoundryReviewSaved"] = PromptMageFoundryReviewSaved
NODE_DISPLAY_NAME_MAPPINGS["PromptMageStudioFoundryReviewSaved"] = "Prompt Mage Studio · Saved Review (Internal)"
from .py.nodes.foundry import PromptMageFoundryReviewOutput
NODE_CLASS_MAPPINGS["PromptMageStudioFoundryReviewOutput"] = PromptMageFoundryReviewOutput
NODE_DISPLAY_NAME_MAPPINGS["PromptMageStudioFoundryReviewOutput"] = "Prompt Mage Studio · Review Output"
from .py.nodes.production_brief import PromptMageGrimoireBrief
NODE_CLASS_MAPPINGS["PromptMageStudioGrimoireBrief"] = PromptMageGrimoireBrief
NODE_DISPLAY_NAME_MAPPINGS["PromptMageStudioGrimoireBrief"] = "Prompt Mage Studio · Production Brief (Internal)"
from .py.nodes.archmage import PromptMageArchmageBeta
NODE_CLASS_MAPPINGS["PromptMageStudioArchmageBeta"] = PromptMageArchmageBeta
NODE_DISPLAY_NAME_MAPPINGS["PromptMageStudioArchmageBeta"] = "Prompt Mage Studio · Archmage (Beta)"
from .py.nodes.appearance import PromptMageStudioAppearanceOverrides
NODE_CLASS_MAPPINGS["PromptMageStudioAppearanceOverrides"] = PromptMageStudioAppearanceOverrides
NODE_DISPLAY_NAME_MAPPINGS["PromptMageStudioAppearanceOverrides"] = "Prompt Mage Studio · Appearance Overrides"
from .py.nodes.resolution import PromptMageResolution
NODE_CLASS_MAPPINGS["PromptMageStudioResolution"] = PromptMageResolution
NODE_DISPLAY_NAME_MAPPINGS["PromptMageStudioResolution"] = "Prompt Mage Studio · Resolution"
from .py.nodes.image_batch import PromptMageStudioImageBatchUpload
NODE_CLASS_MAPPINGS["PromptMageStudioImageBatchUpload"] = PromptMageStudioImageBatchUpload
NODE_DISPLAY_NAME_MAPPINGS["PromptMageStudioImageBatchUpload"] = "Prompt Mage Studio · Upload Images"
from .py.nodes.image_batch import PromptMageStudioImageBatchSelector
NODE_CLASS_MAPPINGS["PromptMageStudioImageBatchSelector"] = PromptMageStudioImageBatchSelector
NODE_DISPLAY_NAME_MAPPINGS["PromptMageStudioImageBatchSelector"] = "Prompt Mage Studio · Server Folder (Advanced)"
from .py.dart.openai_routes import register_openai_routes
register_openai_routes()
from .py.dart.deepseek_routes import register_deepseek_routes
register_deepseek_routes()
from .py.dart.venice_routes import register_venice_routes
register_venice_routes()
from .py.dart.gemini_routes import register_gemini_routes
register_gemini_routes()
from .py.dart.grimoire_routes import register_grimoire_routes
register_grimoire_routes()
from .py.dart.foundry_routes import register_foundry_routes
register_foundry_routes()
