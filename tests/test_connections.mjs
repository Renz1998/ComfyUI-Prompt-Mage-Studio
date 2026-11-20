import assert from "node:assert/strict";
import { connectionsFor, resolveSlot } from "../web/connections.mjs";

const describe = "PromptMageStudioDescribeImage";
assert.equal(connectionsFor('PromptMageStudioImageToText','image','IMAGE',false)[1].type,'PromptMageStudioImageBatchUpload');
assert.equal(connectionsFor('PromptMageStudioImageToText','image','IMAGE',false)[2].type,'PromptMageStudioImageBatchSelector');
assert.equal(connectionsFor('PromptMageStudioImageBatchUpload','image','IMAGE',true)[0].type,'PromptMageStudioArchmageBeta');
assert.deepEqual(connectionsFor('PromptMageStudioImageBatchSelector','filename','STRING',true)[0],{type:'PromptMageStudioArchmageBeta',slot:'source_name'});
assert.deepEqual(connectionsFor(describe,'report','STRING',true),[{type:'PreviewAny',slot:'source'}]);
assert.deepEqual(connectionsFor('PromptMageStudioImageToText','status','STRING',true),[{type:'PreviewAny',slot:'source'}]);
for (const type of [describe, 'PromptMageStudioImageToText']) {
    assert.deepEqual(connectionsFor(type, 'appearance', 'ATELIER_APPEARANCE', false), [{type:'PromptMageStudioAppearanceOverrides',slot:0}]);
}
assert.deepEqual(connectionsFor('PromptMageStudioAppearanceOverrides', 'appearance', 'ATELIER_APPEARANCE', true).map(x => x.slot), ['appearance','appearance','appearance','appearance','appearance']);
assert.equal(connectionsFor('PromptMageStudioSceneComposer','appearance','ATELIER_APPEARANCE',false)[0].type,'PromptMageStudioAppearanceOverrides');
assert.equal(connectionsFor('PromptMageStudioTagComposer','appearance','ATELIER_APPEARANCE',false)[0].type,'PromptMageStudioAppearanceOverrides');
assert.deepEqual(connectionsFor("PromptMageStudioImageToText", "width", "INT", true)[0], { type: "EmptySD3LatentImage", slot: "width" });
assert.deepEqual(connectionsFor("PromptMageStudioImageToText", "height", "INT", true)[0], { type: "EmptySD3LatentImage", slot: "height" });
assert.deepEqual(connectionsFor("PromptMageStudioImageToText", "image", "IMAGE", true)[0], { type: "PreviewImage", slot: "images" });
assert.deepEqual(connectionsFor("PromptMageStudioImageToText", "description", "STRING", true)[0], { type: describe, slot: "description" });
assert.deepEqual(connectionsFor("PromptMageStudioImageToText", "image", "IMAGE", false)[0], { type: "LoadImage", slot: 0 });
assert.deepEqual(connectionsFor("PromptMageStudioGenerate", "STRING", "STRING", true)[0], { type: 'PromptMageStudioArchmageBeta', slot: "source_tags" });
assert.deepEqual(connectionsFor('PromptMageStudioArchmageBeta','source_tags','STRING',false)[0],{type:'PromptMageStudioGenerate',slot:0});
assert.deepEqual(connectionsFor(describe, "source_tags", "STRING", false)[0], { type: "PromptMageStudioGenerate", slot: 0 });
assert.deepEqual(connectionsFor(describe, "prompt", "STRING", true).map((x) => x.type), ["CLIPTextEncode", "PreviewAny"]);
assert.deepEqual(connectionsFor(describe, "general_tags", "STRING", true).map((x) => x.slot), ["general", "source"]);
assert.deepEqual(connectionsFor(describe, "character", "STRING", true)[0], { type: "PromptMageStudioComposePromptV3", slot: "character" });
assert.deepEqual(connectionsFor("PromptMageStudioLoader", "DART_MODEL", "DART_MODEL", true)[0], { type: "PromptMageStudioGenerate", slot: "model" });
assert.deepEqual(connectionsFor("PromptMageStudioGenerate", "tokenizer", "DART_TOKENIZER", false)[0], { type: "PromptMageStudioLoaderV3", slot: 1 });
assert.deepEqual(connectionsFor("PromptMageStudioGenerate", "prompt", "STRING", false)[0], { type: "PromptMageStudioComposePromptV3", slot: 0 });
assert.deepEqual(connectionsFor("AnotherPlugin", "prompt", "STRING", true), []);
const slots = [{ name: "model" }, { name: "tokenizer" }];
assert.equal(resolveSlot(slots, 0).index, 0);
assert.equal(resolveSlot(slots, slots[1]).index, 1);
assert.equal(resolveSlot(slots, "tokenizer").index, 1);
console.log("Connection suggestions passed (including first socket and named inputs).");

const beta='PromptMageStudioArchmageBeta';
assert.equal(connectionsFor(beta,'appearance','ATELIER_APPEARANCE',false)[0].type,'PromptMageStudioAppearanceOverrides');
assert.equal(connectionsFor(beta,'image','IMAGE',false)[1].type,'PromptMageStudioImageBatchUpload');
assert.equal(connectionsFor(beta,'description','STRING',true)[0].slot,'idea');
assert.equal(connectionsFor(beta,'width','INT',true)[0].slot,'width');

assert.equal(connectionsFor("PromptMageStudioGrimoire","production_brief","MAGE_PRODUCTION_BRIEF",true)[0].type,"PromptMageStudioFoundry");
assert.equal(connectionsFor("PromptMageStudioFoundry","production_brief","MAGE_PRODUCTION_BRIEF",false)[0].type,"PromptMageStudioGrimoire");
