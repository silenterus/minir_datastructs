from dataclasses import dataclass
from typing import Optional, List

from minir_datastructs.markdown.comment.comment_kind import ExtractedCommentInstance
from minir_datastructs.markdown.extracted.extracted_block import ExtractedBlock
from minir_datastructs.markdown.extracted.extracted_data_block import ExtractedDataBlock


@dataclass
class ProcessedDataBlock:
    block:      ExtractedBlock
    block_data: ExtractedDataBlock
    extracted_comments: Optional[List[ExtractedCommentInstance]] = None

    is_valid:bool = False

