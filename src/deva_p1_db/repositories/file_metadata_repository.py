from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from deva_p1_db.models import File, FileMetadata


class FileMetadataRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self,
                     file: File,
                     timecode: float,
                     text: str,
                     is_hide: bool = False
                     ) -> Optional[FileMetadata]:
        metadata = FileMetadata(file_id=file.id,
                                timecode=timecode,
                                is_hide=is_hide,
                                text=text)
        self.session.add(metadata)
        await self.session.flush()
        return await self.get_by_id(metadata.id)

    async def get_by_id(self, file_metadata_id: UUID) -> Optional[FileMetadata]:
        stmt = select(FileMetadata).where(FileMetadata.id == file_metadata_id)
        return await self.session.scalar(stmt)

    async def update(self,
                     file_metadata: FileMetadata,
                     is_hide: bool | None = None,
                     text: str | None = None,
                     timecode: float | None = None
                     ) -> None:
        if is_hide is not None:
            file_metadata.is_hide = is_hide
        if text is not None:
            file_metadata.text = text
        if timecode is not None:
            file_metadata.timecode = timecode
        await self.session.flush()



